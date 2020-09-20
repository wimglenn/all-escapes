import os
import sysconfig

from setuptools import setup

site = sysconfig.get_path("purelib")
site = os.path.join(".", site[site.index("lib"):])

setup(
    name="all-escapes",
    url="https://github.com/wimglenn/all-escapes",
    author="Wim Glenn",
    author_email="hey@wimglenn.com",
    license="MIT",
    version="0.1",
    description="Codec for binary escapes",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst; charset=UTF-8",
    py_modules=["all_escapes"],
    data_files=[(site, ['all_escapes.pth'])],
)
