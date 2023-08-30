from setuptools import setup, find_packages

setup(
    name="Termicolor",
    version="0.1.0",
    description="Python styling and coloring for the terminal",
    author="border-l",
    packages=find_packages(),
    install_requires=[
        "colorama"
    ],
)
