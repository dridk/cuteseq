from setuptools import setup, find_packages
import cuteseq

setup(
    name="cuteseq",
    version=cuteseq.__VERSION__,
    description="Un simple exemple d'application écrite avec PySide2",
    author="Sacha Schutz",
    license="GPL3",
    packages=find_packages(),
    install_requires="PySide2",
)
