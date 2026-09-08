from metadata.parse import blurbs


def test_loads_soccer_war_blurb():
    items = blurbs.load()

    assert items == [
        {
            "kind": "season",
            "competition": "American Soccer League (1921-1933)",
            "season": "1928-1929",
            "text": (
                "The Soccer War broke open in 1928–29 after the ASL ordered its clubs "
                "to boycott the National Challenge Cup. Bethlehem Steel, the Newark "
                "Skeeters, and the New York Giants entered anyway; the league suspended "
                "them, and they joined the rival Eastern Soccer League."
            ),
        }
    ]
