from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    Read requirements from a file and return them as a list.
    """
    with open(file_path, "r") as file_obj:
        requirements = [
            req.strip()
            for req in file_obj.readlines()
            if req.strip()
        ]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Keshav",
    author_email="keshavg125@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)