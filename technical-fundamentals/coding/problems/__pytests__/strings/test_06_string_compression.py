from python_solutions.strings import string_compressor


def test_compresses_string_with_repeated_characters():
    assert string_compressor("aabcccccaaa") == "a2b1c5a3"


def test_returns_original_string_if_compression_does_not_reduce_length():
    assert string_compressor("abcde") == "abcde"


def test_returns_empty_string_for_empty_input():
    assert string_compressor("") == ""


def test_returns_single_character_for_string_with_single_character():
    assert string_compressor("a") == "a"


def test_compresses_string_with_uppercase_and_lowercase_letters():
    assert string_compressor("AAAbbbCCCddd") == "A3b3C3d3"


def test_returns_original_string_if_no_repeated_characters():
    assert string_compressor("abcdef") == "abcdef"

