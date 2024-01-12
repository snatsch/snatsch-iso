import os
from setuptools import setup

info = {}
current_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_dir, "iso", "__version__.py"), "r") as file:
    exec(file.read(), info)

with open(os.path.join(current_dir, "README.md"), "r") as fh:
    long_description = fh.read()

setup(
    author=info["__author__"],
    version=info["__version__"],
    description=info["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    name=info["__title__"],
    author_email=info["__author_email__"],
    license=info["__license__"],
    url="https://github.com/snatsch/python-iso",
    keywords="iso iso4217 iso3166",
    packages=["iso"],
    package_data={"iso": ["data/*.csv"]},
    classifiers=(
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ),
)
