from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e.'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove
    return requirements(HYPEN_E_DOT)

setup(
    name='Fault detection',
    version='0.0.1',
    author='andy',
    author_mail='andy@gmail.com',
    install_requiremnets=get_requirements('requirements.txt'),
    packages=find_packages()
)