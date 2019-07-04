import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="mspkc",
    version="0.1",
    author="Stefano Menegon",
    author_email="stefano.menegon@ismar.cnr.it",
    description=("A python client to consume CKAN API and analyze and edit MSP Knowledge Catalogue records"),
    license="GPL3",
    keywords="CKAN MSP Catalogue",
    url="http://todo.todo",
    packages=['mspkc'],
    install_requires=['ckanapi', 'pandas'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
