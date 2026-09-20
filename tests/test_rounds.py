from pathlib import Path
import runpy

import pytest


# Importing metadata.alias also queries MongoDB; this normalizer needs no database.
get_round = runpy.run_path(Path(__file__).parents[1] / 'alias' / 'rounds.py')['get_round']


@pytest.mark.parametrize('label, expected', [
    ('Matchday 1', '1'),
    ('Matchday 46', '46'),
    (' matchday  12 ', '12'),
    ('MATCHDAY\t3', '3'),
    ('Matchday 2 [Apr 24]', '2 [Apr 24]'),
    ('Week 1', '1'),
    (' week  12 ', '12'),
    ('WEEK\t3', '3'),
    ('Week 1 [Nov 1]', '1 [Nov 1]'),
    ('Round 1', '1'),
    ('Round  2', '2'),
    ('Round of 16', '/16'),
    ('Quarterfinals', 'qf'),
    ('Final', 'f'),
    ('Midweek Challenge', 'Midweek Challenge'),
    ('Matchday', 'Matchday'),
    ('Opening Matchday', 'Opening Matchday'),
    ('Week', 'Week'),
    ('Final Week', 'Final Week'),
    ('', ''),
    (3, '3'),
])
def test_round_labels(label, expected):
    assert get_round(label) == expected
    assert get_round(expected) == expected
