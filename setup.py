# This file is placed in the Public Domain.


from setuptools import setup


def read():
    return open("README.rst", "r").read()


setup(
    name="loop",
    version="1",
    url="https://github.com/bthate/loop",
    author="Bart Thate",
    author_email="bthate67@gmail.com",
    description="execute os.popen in sub directories",
    long_description=read(),
    long_description_content_type="text/x-rst",
    license="Public Domain",
    zip_safe=False,
    packages=["loop"],
    scripts=["bin/loop",],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
)
