from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """Read the requirements from a file and return as a list of strings."""
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)        
    return requirements

setup(
    name='mL_project',
    version='0.0.1',
    author='Disha ',
    author_email='dsharminislam@example.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)