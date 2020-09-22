all-escapes
-----------

Registers a codec for representing binary escapes in text domain.

.. code-block:: python

   >>> b"Hello, World!".decode("all-escapes")
   '\\x48\\x65\\x6c\\x6c\\x6f\\x2c\\x20\\x57\\x6f\\x72\\x6c\\x64\\x21'

   >>> r"\x48\x65\x6c\x6c\x6f\x2c\x20\x57\x6f\x72\x6c\x64\x21".encode("all-escapes")
   b'Hello, World!'
