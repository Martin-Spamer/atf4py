from setuptools import setup, find_packages

setup(
    name='atf4py',
    version='0.0.1',
    description='Automated Testing Framework for Python',
    long_description='Automated Testing Framework for Python',
    url='https://github.com/Martin-Spamer/atf4py',
    author='Martin Spamer',
    author_email='Martin@atf4j.net',
    license='GPL',
    packages=find_packages(),
    install_requires=['markdown'],
    include_package_data=True
)
