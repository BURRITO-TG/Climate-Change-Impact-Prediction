from setuptools import setup, find_packages

get_requirements = lambda: open('requirements.txt').read().splitlines()

setup(
    name='climate_change_impact_prediction',
    version='0.1',
    packages=find_packages(),
    author='Bharadwaj',
    install_requires=get_requirements()
)
