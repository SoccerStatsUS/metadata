import hashlib
import os
import random
import time
import unicodedata


def person_identity_key(name):
    name = " ".join(name.split()).casefold()
    name = unicodedata.normalize("NFKD", name)
    return "".join(char for char in name if not unicodedata.combining(char))


def preferred_person_name(current, candidate):
    def accent_count(name):
        decomposed = unicodedata.normalize("NFKD", name)
        return sum(unicodedata.combining(char) != 0 for char in decomposed)

    current = " ".join(current.split())
    candidate = " ".join(candidate.split())
    if accent_count(candidate) > accent_count(current):
        return candidate
    return current



def get_id():
    return hashlib.md5(str(time.time()).encode('utf8')).hexdigest()


def list_paths(root):
    l = []
    for dirname, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.endswith('.py') and fn != '__init__.py':
                l.append(os.path.join(dirname, fn))
    return l


def import_path(p):
    #assert p.endswith('.py')
    #m = p[:-3].replace('/', '.')

    # Use importlib instead?
    #iname = "%s.%s.%s" % (istub, region, xn)
    #m = importlib.import_module(iname)


    return __import__(p, fromlist=["dummy value"]) # __import requires non-empty fromlist to import submodules (foo.bar.baz)
        

def pounds_to_kg(pounds):
    if not pounds:
        return ''

    if pounds == '?':
        return ''

    kg = int(pounds) * 0.45359237
    return int(round(kg, 0))


def inches_to_cm(inches=0, feet=0):
    if not inches and not feet:
        return ''

    if inches == '?' or feet == '?':
        return ''

    feet, inches = int(feet), int(inches)
    real_inches = inches + (feet * 12)
    cm = real_inches * 2.54
    return int(round(cm, 0))
