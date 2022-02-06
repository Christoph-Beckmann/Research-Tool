from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    licensefile = f.read()

setup(
    name='ResearchTool',
    version='0.1.0',
    description='A Tool to summarize text, get keywords and analytics keywords',
    long_description=readme,
    author='Christoph Beckmann',
    author_email='Christoph-Beckmann@outlook.de',
    url='https://github.com/ChristophBeckmann/ResearchTool',
    license=licensefile,
    packages=find_packages(exclude=('tests', 'docs'))
)
