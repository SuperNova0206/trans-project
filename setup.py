from setuptools import setup, find_packages

with open("README.md", "r") as f :
    description = f.read()


setup (
    name="trans",
    version="0.3.0",
    author="SuperNova0206",
    packages=find_packages(),
    install_requires=[
        "typer",
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)