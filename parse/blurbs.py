import os
import tomllib

from metadata.settings import ROOT_DIR


BLURBS = os.path.join(ROOT_DIR, "metadata/data/blurbs.toml")


def load():
    with open(BLURBS, "rb") as f:
        return tomllib.load(f)["blurbs"]
