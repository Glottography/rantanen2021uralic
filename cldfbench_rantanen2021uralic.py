import re
import pathlib
import zipfile
import collections

from csvw.dsv import UnicodeWriter
from clldutils.jsonlib import dump
from cldfgeojson.create import shapely_fixed_geometry
import pyglottography

URL = "https://zenodo.org/records/4784188/files/" \
      "Geographical%20database%20of%20the%20Uralic%20languages.zip?download=1"
GCODES = {  # We fix typos in Glottocodes:
    'sklo1241': 'skol1241',
    'south3253': 'sout3253',
}
GCODE_BY_NAME = {  # Some Glottocodes can be assigned more finegrained, based on dialect info:
    'East Khanty (Surgut Khanty)': 'surg1248',
    'East Khanty (Vakh-Vasyugan Khanty)': 'fare1244',
    'East Mansi': 'east2879',
    'Komi (Izhma dialect group)': 'izhm1234',
    'Komi (Vychegda dialect group)': 'cent2400',
    'Komi (Kosa-Sysola dialect group)': 'sout3379',
    'North Khanty (Obdorsk Khanty)': 'obdo1234',
    'North Khanty (Ob Khanty)': 'khan1273',
}

def shp2geojson(shp):
    import geopandas
    from fiona.crs import from_epsg

    # Re-project to EPSG 4326, aka WGS 84
    data = geopandas.read_file(str(shp))
    data_proj = data.copy()
    data_proj['geometry'] = data_proj['geometry'].to_crs(epsg=4326)
    data_proj.crs = from_epsg(4326)

    for feature in data_proj.__geo_interface__['features']:
        if ' / ' in (feature['properties']['Glottocode'] or ''):
            # A feature is assigned to two languages! We duplicate it.
            assert ' and ' in feature['properties']['Language']
            for gc, name in zip(
                    feature['properties']['Glottocode'].split(' / '),
                    feature['properties']['Language'].split(' and ')):
                props = {k: v for k, v in feature['properties'].items()}
                props.update(Glottocode=gc, Language=name)
                yield shapely_fixed_geometry(dict(
                    type='Feature', geometry=feature['geometry'], properties=props))
        else:
            yield shapely_fixed_geometry(feature)


class Dataset(pyglottography.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "rantanen2021uralic"

    def cmd_download(self, args):
        with self.raw_dir.temp_download(URL, 'ds.zip') as zipp:
            with zipfile.ZipFile(str(zipp)) as zipf:
                zipf.extractall(self.raw_dir)

        geojson = {
            'type': 'FeatureCollection',
            'properties': {
                'dc:description': 'Speaker areas of uralic language varieties in the traditional time period.',
            },
            'features': []
        }

        def normalize_source(s):
            s = s.split(':')[0].strip()
            return re.sub(r'\s+', ' ', s)

        def normalize_props(shp, fid, p):
            #Language, Dialect, Branch, Timeperiod, Otherinfo, Sources, Glottocode, ISO_639_3
            del p['Timeperiod']
            del p['Branch']
            del p['ISO_639_3']
            p['id'] = str(fid)
            p['name'] = p.pop('Language')
            d = p.pop('Dialect')
            if d:
                p['name'] = '{} ({})'.format(p['name'], d)
            p['glottocode'] = p.pop('Glottocode')
            p['glottocode'] = GCODES.get(p['glottocode'], p['glottocode'])
            p['glottocode'] = GCODE_BY_NAME.get(p['name'], p['glottocode'])
            p['year'] = 'traditional'
            p['map_name_full'] = shp.stem
            p['sources'] = p.pop('Sources')
            p['note'] = p.pop('Otherinfo')
            return p

        fid, sources, props = 0, collections.Counter(), []
        for shp in self.raw_dir.joinpath(
                'Geographical database of the Uralic languages',
                'Geospatial datasets',
                'Language distributions',
                'Expert distributions',
                'Languages').glob('*_traditional_OGUL.shp'):
            for v in shp2geojson(shp):
                sources.update([normalize_source(s) for s in v['properties']['Sources'].split(',') if s.strip()])
                fid += 1
                nprops = normalize_props(shp, fid, v['properties'])
                props.append(nprops)
                v['properties'] = nprops
                geojson['features'].append(v)

        with UnicodeWriter(self.etc_dir / 'features.csv') as w:
            w.writerows(props)

        dump(geojson, self.raw_dir / 'dataset.geojson', indent=2)
