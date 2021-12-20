
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='outputformater',
    version='0.0.1',
    description='Decorate and beautify strings',
    long_description=readme,
    author='Felipe Delestro',
    author_email='delestro@gmail.com',
    url='https://github.com/delestro/outputformater',
    license=license,
    packages=find_packages()
)
