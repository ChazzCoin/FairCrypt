from setuptools import setup, find_packages
import os

current = os.getcwd()

setup(
    name='FairCrypt',
    version='1.0.0',
    description='Data Structure Helper Functions. Wrappers. Callbacks. Threading. FFMPEG',
    url='https://github.com/chazzcoin/FairCrypt',
    author='ChazzCoin',
    author_email='chazzcoin@gmail.com',
    license='BSD 2-clause',
    packages=find_packages(),
    install_requires=['python-dateutil>=2.7.5'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)