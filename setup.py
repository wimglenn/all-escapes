import os

from setuptools import setup
from setuptools.command.install import install


class Install(install):

    def initialize_options(self):
        install.initialize_options(self)
        self.extra_path = "all-escapes", "import all_escapes\n"

    def finalize_options(self):
        install.finalize_options(self)
        install_suffix = os.path.relpath(self.install_lib, self.install_libbase)
        if install_suffix == self.extra_path[1]:
            self.install_lib = self.install_libbase


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
    cmdclass={"install": Install},
    options={"bdist_wheel": {"universal": True}},
)
