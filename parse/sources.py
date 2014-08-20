import os

from soccerdata.settings import ROOT_DIR

SOURCE_PATH = os.path.join(ROOT_DIR, 'soccerdata/data/sources')

print(SOURCE_PATH)


def load():

    def process_line(line):
        if not line.strip():
            return {}


        fields = line.split(';')
        fields = [e.strip() for e in fields]
        if len(fields) == 2:
            name, author = fields
            url = ''
        else:
            try:
                name, author, url = fields
            except:
                import pdb; pdb.set_trace()

        d = {
                'name': name,
                'author': author,
                'base_url': url,
                }

        if 'www.' in url:
            url2 = url.replace('www.', '')
            d2 = d.copy()
            d2['base_url'] = url2
            return [d, d2]
        else:
            return [d]

    l = []

    for line in open(SOURCE_PATH):
        l.extend(process_line(line))

    return [e for e in l if e]

