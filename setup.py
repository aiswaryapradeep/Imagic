

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='imagic',
    description='image resizer converter cli',
    long_description=readme,
    author='Aiswarya Pradeep',
    url='https://github.com/aiswaryapradeep/Imagic',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

