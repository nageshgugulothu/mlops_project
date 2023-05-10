from setuptools import setup, find_packages
from typing import List

HYPEN_EDOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements =f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_EDOT in requirements:
            requirements.remove(HYPEN_EDOT)

    return requirements


setup(
    name = 'mlops_project',
    version= '0.0.1',
    author = 'Nageshwar',
    author_email= 'nageshgugulothu@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)