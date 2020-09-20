import codecs
import sys

# Kevin's original paste: https://pastebin.com/kXSdqu4k

def decode_py2(some_bytes, errors="strict"):
    s = "".join(r"\x{:02x}".format(ord(i)) for i in some_bytes)
    return (s, len(some_bytes))

def decode_py3(some_bytes, errors="strict"):
    s = "".join(r"\x{:02x}".format(i) for i in some_bytes)
    return (s, len(some_bytes))

def encode(some_string, errors="strict"):
    if len(some_string) % 4 != 0:
        raise ValueError("Expected only four-character escape sequences")
    chars = []
    for i in range(0, len(some_string), 4):
        symbol = some_string[i:i+4]
        if symbol[:2] != r"\x":
            raise ValueError(r"Expected only \x escape sequences")
        chars.append(int(symbol[2:], 16))
    return (bytes(bytearray(chars)), len(some_string))

if sys.version_info < (3,):
    AllEscapes = codecs.CodecInfo(encode, decode_py2, name="all-escapes")
else:
    AllEscapes = codecs.CodecInfo(encode, decode_py3, name="all-escapes")

def search_function(name):
    """Passed to codecs.register to register our codec search function.

    Search functions are expected to take one argument, the encoding name in
    all lower case letters, and either return None, or a tuple of functions
    (encoder, decoder, stream_reader, stream_writer) or a CodecInfo instance.
    """
    if name == "all-escapes":
        return AllEscapes

codecs.register(search_function)
