from setuptools import find_packages, setup

setup(
    name='py_matrice',
    packages=find_packages(include=['py_matrice']),
    version='0.1.0',
    description='A simple matrix library in Python.',
    author='NoobJsPerson',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)