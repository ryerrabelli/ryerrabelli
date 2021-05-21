#!/bin/sh

# To change the permissions of this file so it can be run in terminal, do
# chmod 755 upload_to_pypi.sh

# To run, cd to the main project folder and run:
# ./scripts/upload_to_pypi.sh
# PyPI token credentials should be saved to $HOME/.pypirc in order to not have to type in the username and password
# The username will be __token__. Password will be a long case-sensitive alphanumeric string starting with pypi-
# twine should also aleady be installed i.e. by
# $ pip install twine
#

echo Uploading to pypi

# First make sure that the latest version of the code is committed (not dirty) and tagged.
# Then make sure you have an egg file and a dist folder.
# To get this, run
# python setup.py install
git commit -a --message "test commit by terminal"
python setup.py install
#PYTHONPATH="src" python -m ryerrabelli.__init__
# You should do this again if you change the code/add tags/etc so it can update.
#python -m twine upload --repository testpypi dist/*
#python -m twine upload dist/*


echo Done.