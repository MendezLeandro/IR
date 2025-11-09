from python_solutions.strings import is_substring


def test_rotates_a_string():
    assert is_substring("Hello", "oHell") is True


def test_rotates_another_string():
    assert is_substring("waterbottle", "erbottlewat") is True

