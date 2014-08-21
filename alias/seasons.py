
aliases = {}


def get_season(s):
    if s is None:
        return None

    
    s = s.strip()

    s = s.replace('Finalizacion', 'Finalización').replace('Adecuacion', 'Adecuación')

    return aliases.get(s, s)
