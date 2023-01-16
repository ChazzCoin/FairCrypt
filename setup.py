from setuptools import setup, find_packages
import os

current = os.getcwd()

setup(
    name='FairCrypt',
    version='1.6.0',
    description='Basic Encryption Functions and Wrappers',
    url='https://github.com/chazzcoin/FairCrypt',
    author='ChazzCoin',
    author_email='chazzcoin@gmail.com',
    license='BSD 2-clause',
    packages=find_packages(),
    install_requires=['python-dateutil>=2.7.5', 'FairResources>=5.2.0'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)