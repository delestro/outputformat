from setuptools import setup

long_description = "It is recommended to use ouf as shortcut for outputformat import outputformat as ouf\n"
long_description += "Main functions are:\n"
long_description += "* ouf.boxtitle\n"
long_description += "* ouf.linetitle\n"
long_description += "* ouf.bigtitle\n"
long_description += "* ouf.showlist\n"
long_description += "* ouf.bar\n"
long_description += "* ouf.barlist\n"
long_description += "By default, functions print the result\n."
long_description += "You have the alternative to return a string instead, by passing the argument return_str=True\n"
long_description += "(nothing will be printed in this case)."

setup(
    name="outputformat",
    packages=["outputformat"],
    version="0.1.1",
    description="Decorate and beautify output",
    long_description=long_description,
    author="Felipe Delestro",
    author_email="delestro@gmail.com",
    url="https://github.com/delestro/outputformat",
    download_url="https://github.com/delestro/outputformat/archive/refs/tags/v0.1.1.tar.gz",
    license="MIT",
    keywords=["output", "print", "decorate", "format", "string", "beautify"],
    python_requires=">=3.6",
)
