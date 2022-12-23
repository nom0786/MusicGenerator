from setuptools import setup, find_packages

setup(
    name='MusicGenerator',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A Python package designed to turn randomly selected notes into a melody based on statistics.',
	url='https://github.com/nom0786/MusicGenerator',
    author='Nyx Zhang & Noman Mohammad',
    author_email='petitmi001@gmail.com'
)
