from python_solutions.strings import is_one_away


def test_one_away_replace():
    assert is_one_away("pale", "bale") is True
    assert is_one_away("bbaa", "bcca") is False


def test_one_away_insert():
    assert is_one_away("pale", "ple") is True


def test_one_away_remove():
    assert is_one_away("pale", "pales") is True


def test_same_strings():
    assert is_one_away("abc", "abc") is True


def test_more_than_one_edit_away():
    assert is_one_away("abcd", "efgh") is False


def test_more_than_one_edit_away_2():
    assert is_one_away("palesa", "pale") is False


def test_empty_strings():
    assert is_one_away("", "") is True


def test_one_character_difference():
    assert is_one_away("a", "ab") is True


def test_empty_and_non_empty_string():
    assert is_one_away("", "a") is True

