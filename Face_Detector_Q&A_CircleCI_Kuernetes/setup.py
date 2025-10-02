from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements= f.read().splitlines()

setup(
    name='Face Detector and Q&A',
    version= "0.1",
    author= "Om Bhandwalkar",
    packages= find_packages(),
    install_requires= requirements
)