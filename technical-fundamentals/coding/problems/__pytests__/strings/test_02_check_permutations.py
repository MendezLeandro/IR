from python_solutions.strings import is_permutation


def test_returns_true_for_permutations_with_same_length_strings():
    assert is_permutation("abc", "cba") is True


def test_returns_false_for_strings_with_different_lengths():
    assert is_permutation("abc", "cbad") is False


def test_returns_true_for_permutations_with_special_characters():
    assert is_permutation("abc!", "!bac") is True


def test_returns_false_for_non_permutations_with_special_characters():
    assert is_permutation("abc!", "!bcd") is False


def test_returns_true_for_empty_strings():
    assert is_permutation("", "") is True


def test_returns_true_for_long_strings_with_same_characters():
    assert is_permutation("a" * 1000, "a" * 1000) is True


def test_returns_false_for_long_strings_with_different_characters():
    assert is_permutation("a" * 1000, "b" * 1000) is False

