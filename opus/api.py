# -*- coding: utf-8 -*-
'''
OPUS API class
'''

import requests

from .url import clean
from .data import Data
from .metadata import Metadata
from .images import Images, Image
from .files import Files, File
from .mults import Mults
from .range import Range
from .fields import Fields, Field
from .categories import Categories, Category

API_URL = 'https://tools.pds-rings.seti.org/opus/api'

FMT = ['json', 'html', 'zip', 'csv']

class API(object):
    '''OPUS Seti Ring-Node API class'''

    def __init__(self, url=API_URL, verbose=False):
        self.url = clean(url)
        self.verbose = verbose

    def __str__(self):
        return self.url

    def __repr__(self):
        return "OPUS Seti Ring-Node API: {}".format(self.url)

    def request(self, entry, fmt='json', **kwargs):
        if fmt not in FMT:
            raise ValueError(
                "Format '{}' not in {}".format(fmt, FMT)
            )

        params = ''
        if len(kwargs) != 0:
            params = '?' + '&'.join(
                '{}={}'.format(key, value)
                for key, value in kwargs.items()
            )

        return self.url + entry + '.' + fmt + params

    def load(self, entry, **kwargs):
        url = self.request(entry, fmt='json', **kwargs)
        if self.verbose:
            print('Call to: {}'.format(url))

        response = requests.get(url)
        if response.ok:
            return response.json()
        else:
            raise RuntimeError('The request at {} failed'.format(url))

    def count(self, **kwargs):
        '''Get result count for a search'''
        res = self.load('meta/result_count', **kwargs)
        return int(res['data'][0]['result_count'])

    def data(self, limit=100, page=1, **kwargs):
        '''Get data for a search'''
        if limit is None:
            kwargs['limit'] = self.count(**kwargs)
        else:
            kwargs['limit'] = limit
            kwargs['page'] = page
        return Data(self.load('data', **kwargs))

    def metadata(self, opus_id):
        '''Get detail for a single observation'''
        return Metadata(self.load('metadata_v2/'+opus_id))

    def images(self, size='med', limit=100, page=1, **kwargs):
        '''Get image results for a search'''
        size = size.lower()
        if size not in ['thumb', 'small', 'med', 'full']:
            raise ValueError(
                'Image size {} unknown (available: [thumb,small,med,full])'.format(size))

        if limit is None:
            kwargs['limit'] = self.count(**kwargs)
        else:
            kwargs['limit'] = limit
            kwargs['page'] = page
        return Images(self.load('images/'+size, **kwargs), size)

    def image(self, opus_id, size='med'):
        '''Get images for a single observation'''
        size = size.lower()
        if size not in ['thumb', 'small', 'med', 'full']:
            raise ValueError(
                'Image size {} unknown (available: [thumb,small,med,full])'.format(size))

        json = self.load('image/'+size+'/'+opus_id)
        return Image(opus_id, json['path'], json['data'][0]['img'])

    def file(self, opus_id):
        '''Get files for a single observation'''
        json = self.load('files/'+opus_id)
        return File(opus_id, json['data'][opus_id])

    def files(self, limit=100, page=1, **kwargs):
        '''Get all files results for a search'''
        if limit is None:
            kwargs['limit'] = self.count(**kwargs)
        else:
            kwargs['limit'] = limit
            kwargs['page'] = page
        return Files(self.load('files', **kwargs))

    def mults(self, param='target', **kwargs):
        '''Returns all possible values for a given multiple choice
        field, given a search, and the result count for each value'''
        return Mults(self.load('meta/mults/'+param, **kwargs))

    def range(self, param='RINGGEOringradius1', **kwargs):
        '''Get range endpoints for a field, given a search'''
        return Range(param, self.load('meta/range/endpoints/'+param, **kwargs))

    def field(self, field):
        '''Get information about a particular field'''
        return Field(field, self.load('fields/'+field)['data'][field])

    def fields(self):
        '''Get list of all fields'''
        return Fields(self.load('fields')['data'])

    def category(self, opus_id):
        '''Get all fields in a category'''
        return Categories(self.load('categories/'+opus_id))

    def categories(self):
        '''List category names'''
        return Categories(self.load('categories'))
