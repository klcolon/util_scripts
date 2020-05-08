from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

__author__ = "Katsuya Colón"
__version__ = "0.0.3"
__email__ = "kcolon@caltech.edu"

setup(
    name='single_cell_analysis',
    version=__version__ ,
    author=__author__ ,
    author_email=__email__ ,
    description='A package for feature barcode and single cell analysis from single cell data',
    long_description=long_description,
    long_description_content_type='ext/markdown',
    packages=find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
