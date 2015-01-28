try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as file:
    long_description = file.read()

setup(
    name='montecarlo',
    version='0.1',
    description='A small Python module to quickly create simple Monte Carlo simulations.',
    long_description=long_description,
    author='Christopher Su',
    author_email='chris+py@christopher.su',
    url='https://github.com/csu/pymontecarlo',
    packages=['montecarlo'],
)