from setuptools import setup, find_packages

setup(
    name='recsort',
    version='0.6',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA hack-a-thon python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/ShivaanSook/recsort',
    author='Shivaan Sook',
    author_email='shivaansook6@gmail.com'
)