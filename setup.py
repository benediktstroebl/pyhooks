from setuptools import setup

setup(
    name="pyhooks",
    version="0.1.3",
    packages=["pyhooks"],
    install_requires=open("requirements.txt").read().splitlines(),
)
