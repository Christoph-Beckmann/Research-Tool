from setuptools import setup, find_packages

with open('README.md') as f:
    readme_file = f.read()

with open('LICENSE') as f:
    license_file = f.read()

setup(
    name='ResearchTool',
    version='0.1.0',
    description='A Tool to summarize text, get keywords and analytics keywords',
    long_description=readme_file,
    author='Christoph Beckmann',
    author_email='Christoph-Beckmann@outlook.de',
    url='https://github.com/ChristophBeckmann/ResearchTool',
    license=license_file,
    packages=find_packages(exclude=('tests', 'docs'))
)
