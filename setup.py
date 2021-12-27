from setuptools import setup


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="outputformater",
    packages=["outputformater"],
    version="0.1.0",
    description="Decorate and beautify output",
    long_description=readme,
    author="Felipe Delestro",
    author_email="delestro@gmail.com",
    url="https://github.com/delestro/outputformater",
    download_url="https://github.com/delestro/outputformater/archive/refs/tags/v0.1.0.tar.gz",
    license=license,
    keywords=["output", "print", "decorate", "format", "string", "beautify"],
    python_requires=">=3.6",
)
