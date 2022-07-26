

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# this grabs the requirements from requirements.txt
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setuptools.setup(
    name='py_secureapikeys_azumio',
    version='0.0.3',
    author='Igor Rendulic',
    author_email='igor@azumio.com',
    description='Azumio Secure API Keys',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/azumio/secureapikeys',
    project_urls={
        "Bug Tracker": "https://github.com/azumio/secureapikeys/issues"
    },
    license='Apache 2.0',
    packages=['py_secureapikeys_azumio'],
    install_requires=REQUIREMENTS,
)
