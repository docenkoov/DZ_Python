import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("hello", "Hello"),
        ("Hello", "Hello"),
        ("hello world", "Hello world"),
        ("", ""),
        (" ", ""),
        ("python", "Python"),
        ("123abc", "123abc"),
    ],
)
def test_capitilize_positive(input_text, expected_output):
    assert string_utils.capitilize(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (None, ""),
        (" ", ""),
    ],
)
def test_capitilize_negative(input_text, expected_output):
    assert string_utils.capitilize(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("   hello", "hello"),
        ("hello   ", "hello"),
        ("   ", ""),
        ("", ""),
        ("   leading and trailing spaces   ", "leading and trailing spaces"),
    ],
)
def test_trim_positive(input_text, expected_output):
    assert string_utils.trim(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (None, ""),
        (" ", ""),
    ],
)
def test_trim_negative(input_text, expected_output):
    assert string_utils.trim(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("a,b,c", ["a", "b", "c"]),
        ("", []),
        ("   ", []),
        ("1,2,3", ["1", "2", "3"]),
        ("apple,banana,orange", ["apple", "banana", "orange"]),
        (":::", ":"),
        (",,,", ["", "", "", ""]),
    ],
)
def test_to_list_positive(input_text, expected_output):
    assert string_utils.to_list(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (None, []),
        (" ", []),
    ],
)
def test_to_list_negative(input_text, expected_output):
    assert string_utils.to_list(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("hello", "h", True),
        ("hello", "z", False),
        ("", "", True),
        ("", "h", False),
        ("123abc", "1", True),
        ("hello world", " ", True),
    ],
)
def test_contains_positive(input_text, symbol, expected_output):
    assert string_utils.contains(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        (None, "h", False),
        ("", None, False),
        (" ", "z", False),
    ],
)
def test_contains_negative(input_text, symbol, expected_output):
    assert string_utils.contains(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("hello world", "o", "hell wrld"),
        ("hello", "z", "hello"),
        ("", "z", ""),
        ("123abc", "1", "23abc"),
        ("hello", "", "hello"),
    ],
)
def test_delete_symbol_positive(input_text, symbol, expected_output):
    assert string_utils.delete_symbol(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        (None, "h", ""),
        ("", None, ""),
        (" ", "z", " "),
    ],
)
def test_delete_symbol_negative(input_text, symbol, expected_output):
    assert string_utils.delete_symbol(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("hello", "h", True),
        ("hello", "z", False),
        ("", "", True),
        ("", "h", False),
    ],
)
def test_starts_with_positive(input_text, symbol, expected_output):
    assert string_utils.starts_with(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        (None, "h", False),
        ("", None, False),
    ],
)
def test_starts_with_negative(input_text, symbol, expected_output):
    assert string_utils.starts_with(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("hello", "o", True),
        ("hello", "z", False),
        ("", "", True),
        ("", "h", False),
    ],
)
def test_end_with_positive(input_text, symbol, expected_output):
    assert string_utils.end_with(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        (None, "h", False),
        ("", None, False),
    ],
)
def test_end_with_negative(input_text, symbol, expected_output):
    assert string_utils.end_with(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("", True),
        (" ", True),
        ("hello", False),
        ("   ", True),
        ("SkyPro", False),
    ],
)
def test_is_empty_positive(input_text, expected_output):
    assert string_utils.is_empty(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (None, True),
    ],
)
def test_is_empty_negative(input_text, expected_output):
    assert string_utils.is_empty(input_text) == expected_output


@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([], ""),
        (["a", "b"], "a, b"),
        ([1, 2, 3], "1, 2, 3"),
        (["apple", "banana"], "apple, banana"),
    ],
)
def test_list_to_string_positive(input_list, expected_output):
    assert string_utils.list_to_string(input_list) == expected_output


@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        (None, ""),
    ],
)
def test_list_to_string_negative(input_list, expected_output):
    assert string_utils.list_to_string(input_list) == expected_output
