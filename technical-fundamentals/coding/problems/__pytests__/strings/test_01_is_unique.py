from python_solutions.strings import is_unique


def test_returns_true_for_unique_characters():
    assert is_unique("abc") is True
    assert is_unique("abcdefg") is True
    assert is_unique("123456") is True
    assert is_unique("!@#$%^") is True


def test_returns_false_for_non_unique_characters():
    assert is_unique("aab") is False
    assert is_unique("hello") is False
    assert is_unique("testing") is False
    assert is_unique("1234456") is False
    assert is_unique("abccdef") is False


def test_returns_true_for_empty_string():
    assert is_unique("") is True


def test_handles_whitespace_correctly():
    assert is_unique("a b c") is False
    assert is_unique("ab c") is True


def test_handles_mixed_case_correctly():
    assert is_unique("aA") is True
    assert is_unique("Aa") is True
    assert is_unique("Hello") is False

