from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT= "-e ."
def get_requirements(file_path:str) -> List[str]:
    requirements=[]
    with open(file_path,'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(

    name="credit_card_fraud_detection",
    version="0.0.1",
    author="Anshul",
    author_email="anshul.mehra5555@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('/Users/anshulmehra/credit_card_fault_detection/requirements.txt')
)