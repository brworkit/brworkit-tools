import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pkgname",
    version="0.0.2",
    author="brworkit",
    author_email="brworkit@gmail.com",
    description="A python package for ...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brworkit/python-package-pkgname.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)