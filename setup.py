from setuptools import find_packages, setup

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name='end-to-end-ml-prj',
    version = '0.0.1',
    author = 'Sesandu',
    author_email='sesandu21@gmail.com',
    install_requires = get_requirements('requirements.txt')
)