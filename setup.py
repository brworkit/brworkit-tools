import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="brworkittools",
    version="0.0.6",
    author="brworkit",
    author_email="brworkit@gmail.com",
    description="A python package for avoid repetitions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brworkit/brworkit-tools.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)