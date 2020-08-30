import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fakenamegenerator_API",  # Replace with your own username
    version="0.0.1",
    author="Catarium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/catarium/fakenamegenerator_API",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
