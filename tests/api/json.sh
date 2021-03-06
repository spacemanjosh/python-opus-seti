# Download JSON outputs from OPUS API
root=$(git rev-parse --show-toplevel)

wget -nv -O $root/tests/api/meta/result_count.json 'https://tools.pds-rings.seti.org/opus/api/meta/result_count.json?planet=Saturn&target=pan'
wget -nv -O $root/tests/api/data.json 'https://tools.pds-rings.seti.org/opus/api/data.json?planet=Saturn&target=pan&limit=10&page=2'
wget -nv -O $root/tests/api/data_all.json 'https://tools.pds-rings.seti.org/opus/api/data.json?planet=Saturn&target=pan&limit=1636'
wget -nv -O $root/tests/api/data_vims.json 'https://tools.pds-rings.seti.org/opus/api/data.json?instrumentid=Cassini+VIMS&target=TITAN&COVIMSswathlength1=2&COVIMSswathwidth1=2&order=time1&cols=opusid,target,revno,time1,primaryfilespec&limit=10&page=1'
wget -nv -O $root/tests/api/metadata_v2/COISS_2001-1459551663_1459568594-N1459551972_1.json 'https://tools.pds-rings.seti.org/opus/api/metadata_v2/COISS_2001-1459551663_1459568594-N1459551972_1.json'
wget -nv -O $root/tests/api/images/med.json 'https://tools.pds-rings.seti.org/opus/api/images/med.json?planet=Saturn&target=pan&limit=10&page=2'
wget -nv -O $root/tests/api/image/med/COISS_2001-1459551663_1459568594-N1459551972_1.json 'https://tools.pds-rings.seti.org/opus/api/image/med/COISS_2001-1459551663_1459568594-N1459551972_1.json'
wget -nv -O $root/tests/api/files/COISS_2001-1459551663_1459568594-N1459551972_1.json 'https://tools.pds-rings.seti.org/opus/api/files/COISS_2001-1459551663_1459568594-N1459551972_1.json'
wget -nv -O $root/tests/api/files/COVIMS_0020-2007137T054828_2007143T180509-v1558621524_1_VIS.json 'https://tools.pds-rings.seti.org/opus/api/files/COVIMS_0020-2007137T054828_2007143T180509-v1558621524_1_VIS.json'
wget -nv -O $root/tests/api/files.json 'https://tools.pds-rings.seti.org/opus/api/files.json?planet=Saturn&target=pan&limit=10&page=2'
wget -nv -O $root/tests/api/meta/range/endpoints/RINGGEOringradius1.json 'https://tools.pds-rings.seti.org/opus/api/meta/range/endpoints/RINGGEOringradius1.json?target=Saturn'
wget -nv -O $root/tests/api/categories/COISS_2001-1459551663_1459568594-N1459551972_1.json 'https://tools.pds-rings.seti.org/opus/api/categories/COISS_2001-1459551663_1459568594-N1459551972_1.json'
wget -nv -O $root/tests/api/categories.json 'https://tools.pds-rings.seti.org/opus/api/categories.json?surfacegeometrytargetname=Methone'
wget -nv -O $root/tests/api/fields/target.json 'https://tools.pds-rings.seti.org/opus/api/fields/target.json'
wget -nv -O $root/tests/api/fields.json 'https://tools.pds-rings.seti.org/opus/api/fields.json'
