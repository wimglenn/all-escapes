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
