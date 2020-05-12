from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

__author__ = "Katsuya Colón"
__version__ = "0.0.2"
__email__ = "kcolon@caltech.edu"

setup(
    name='general data analysis',
    version=__version__ ,
    author=__author__ ,
    author_email=__email__ ,
    description='A package for general data analysis',
    long_description=long_description,
    long_description_content_type='ext/markdown',
    packages=find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
