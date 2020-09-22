import codecs
import sys

# Adapted from Kevin's original paste: https://pastebin.com/kXSdqu4k

if sys.version_info >= (3,):
    # bytestrings already iterate as integers in py3
    ord = lambda v: v

def decode(some_bytes, errors="strict"):
    s = "".join(r"\x{:02x}".format(ord(i)) for i in some_bytes)
    return s, len(some_bytes)

def encode(some_string, errors="strict"):
    if len(some_string) % 4 != 0:
        raise ValueError("Expected only four-character escape sequences")
    chars = []
    for i in range(0, len(some_string), 4):
        symbol = some_string[i:i+4]
        try:
            val = int(symbol[2:], 16)
        except ValueError:
            val = None
        if symbol[:2] != r"\x" or val is None:
            if errors == "strict":
                raise ValueError(r"Expected only \x escape sequences")
            elif errors == "replace":
                val = 0x3F  # codepoint of "?"
            elif errors == "ignore":
                continue
            else:
                raise LookupError("unknown error handler name %r" % errors)
        chars.append(val)
    return bytes(bytearray(chars)), len(some_string)

AllEscapes = codecs.CodecInfo(encode, decode, name="all-escapes")

def search_function(name):
    """Passed to codecs.register to make our codec available.

    Search functions are expected to take one argument, the encoding name in
    all lower case letters, and either return None, or a tuple of functions
    (encoder, decoder, stream_reader, stream_writer) or a CodecInfo instance.
    """
    if name.replace("_", "-") == "all-escapes":
        return AllEscapes

codecs.register(search_function)
