from python_solutions.strings import is_palindrome_permutation


def test_empty_string():
    assert is_palindrome_permutation("") is True


def test_single_character_string():
    assert is_palindrome_permutation("a") is True


def test_palindrome_with_odd_length():
    assert is_palindrome_permutation("taco cat") is True


def test_palindrome_with_even_length():
    assert is_palindrome_permutation("rdeder") is True


def test_non_palindrome_with_odd_length():
    assert is_palindrome_permutation("hello") is False


def test_non_palindrome_with_even_length():
    assert is_palindrome_permutation("world") is False


def test_string_with_mixed_case():
    assert is_palindrome_permutation("RaceCar") is True


def test_string_with_non_alphanumeric_characters():
    assert is_palindrome_permutation("12321") is True


def test_string_with_no_possible_palindrome_permutation():
    assert is_palindrome_permutation("abcdefg") is False

