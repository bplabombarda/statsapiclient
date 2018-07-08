import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="statsapiclient",
    version="0.0.1",
    author="Brett LaBombarda",
    author_email="bplabombarda@gmail.com",
    description="A client for the NHL stats API",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/bplabombarda/statsapiclient",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ),
)