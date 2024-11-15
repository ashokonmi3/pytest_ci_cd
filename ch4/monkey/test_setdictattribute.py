import pytest

# A simple Cheese class for demonstration purposes


class Cheese:
    def __init__(self):
        # _default_prefs is a dictionary holding different preferences
        self._default_prefs = {
            "slicing": ["cheddar"],
            "spreadable": ["cream cheese"],
            "salads": ["mozzarella"]
        }

# Test function using monkeypatch.setitem


def test_monkeypatch_setitem(monkeypatch):
    cheese = Cheese()

    # Print initial dictionary values
    print(f"Initial prefs: {cheese._default_prefs}")

    # Monkeypatch the _default_prefs dictionary and change some items
    monkeypatch.setitem(cheese._default_prefs, "slicing", ["provolone"])
    monkeypatch.setitem(cheese._default_prefs, "spreadable", ["brie"])
    monkeypatch.setitem(cheese._default_prefs, "salads", ["pepper jack"])

    # Print modified dictionary values
    print(f"Modified prefs: {cheese._default_prefs}")

    # Assertions to check that values were modified correctly
    assert cheese._default_prefs["slicing"] == ["provolone"]
    assert cheese._default_prefs["spreadable"] == ["brie"]
    assert cheese._default_prefs["salads"] == ["pepper jack"]
