# project setup. Based on example here:

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Scraping package',
    long_description=readme,
    author='Omodayo Origunwa',
    author_email='dayo1523@gmail.com',
    url='https://github.com/dinoDayo/scraping.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)