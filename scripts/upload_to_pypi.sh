#!/bin/sh

# To change the permissions of this file so it can be run in terminal, do
# chmod 755 upload_to_pypi.sh

# To run, cd to the main project folder and run:
# ./scripts/upload_to_pypi.sh
# PyPI token credentials should be saved to $HOME/.pypirc
# The username will be __token__. Password will be a long case-sensitive alphanumeric string starting with pypi-
#

echo Uploading to pypi

# first make sure you have an egg file and a dist folder. To get this, run setup.py install
#python3 -m twine upload --repository testpypi dist/*
python3 -m twine upload dist/*


echo Done.