import os
from setuptools import setup

info = {}
current_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_dir, "iso", "__version__.py"), "r") as file:
    exec(file.read(), info)

setup(
    author=info["__author__"],
    version=info["__version__"],
    description=info["__description__"],
    name=info["__title__"],
    author_email=info["__author_email__"],
    license=info["__license__"],
    python_requires=">=3.7.*",
    packages=["iso"],
    package_data={"iso": ["data/*.csv"]},
    classifiers=(
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ),
)
