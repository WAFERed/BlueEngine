from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    return requirements

setup(
    name='blue',
    version='0.7.3',
    author='Syed Mustafa Ahmed, Talha Lodhi, Mohammad Ibrahim',
    author_email='syedmustafaahmad@gmail.com',
    long_description=open("README.md","rt").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/WAFERed/BlueEngine",
    license="GPLv3",
    packages=find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points='''
    [console_scripts]
    blue=blue.cli:cli
    '''
)