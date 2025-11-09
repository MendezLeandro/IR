from python_solutions.strings import urlify


def test_replaces_spaces_in_a_string_with_percent20():
    assert urlify("ab c") == "ab%20c"


def test_handles_leading_and_trailing_spaces():
    assert urlify("  ab c  ") == "%20%20ab%20c%20%20"


def test_returns_empty_string_when_input_is_empty():
    assert urlify("") == ""


def test_does_not_modify_string_without_spaces():
    assert urlify("abc") == "abc"


def test_handles_multiple_consecutive_spaces():
    assert urlify("a  b   c") == "a%20%20b%20%20%20c"


def test_handles_special_characters():
    assert urlify("a b!c") == "a%20b!c"


def test_mr_3ohn_smith():
    assert urlify("Mr 3ohn Smith") == "Mr%203ohn%20Smith"

