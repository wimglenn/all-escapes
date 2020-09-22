import pytest

import all_escapes


def test_decode():
    x = b"Hello, World!"
    escapes = x.decode("all-escapes")
    assert escapes == r"\x48\x65\x6c\x6c\x6f\x2c\x20\x57\x6f\x72\x6c\x64\x21"


def test_encode():
    escapes = r"\x48\x65\x6c\x6c\x6f\x2c\x20\x57\x6f\x72\x6c\x64\x21"
    x = escapes.encode("all-escapes")
    assert x == b"Hello, World!"


def test_decode_empty():
    assert b"".decode("all-escapes") == u""


def test_encode_empty():
    assert u"".encode("all-escapes") == b""


def test_bad_value_len():
    val = r"\x48\x1"
    with pytest.raises(ValueError, match="only four-character"):
        val.encode("all-escapes")


def test_bad_value_esc():
    val = r"\x48aaaa"
    with pytest.raises(ValueError, match=r"only \\x"):
        val.encode("all-escapes")


def test_error_handler_ignore():
    escapes = r"\x48\xFG\x6c"
    x = escapes.encode("all-escapes", errors="ignore")
    assert x == b"Hl"


def test_error_handler_replace():
    escapes = r"\x48\xFG\x6c"
    x = escapes.encode("all-escapes", errors="replace")
    assert x == b"H?l"


def test_bad_err_handler():
    val = r"\x48aaaa"
    with pytest.raises(LookupError, match=r"unknown error handler"):
        val.encode("all-escapes", errors="wtf")
