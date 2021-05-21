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


# First make sure that the latest version of the code is committed (not dirty) and tagged.
# Then make sure you have an egg file and a dist folder.
# To get this, run
# python setup.py install
echo Committing
git commit -a --message "test commit by terminal"


echo Getting and bumping up the version
# First two options return returns 1.0.4+3.ge1ca766.dirty
#python -c "import versioneer; print(versioneer.get_version())"
#PYTHONPATH="src" python -m ryerrabelli.__init__   # relies on calling of the module to return versioneer version (I added it to the init__ file)
export DESCRIBE=$(git describe --always --tags --long --first-parent)   # returns something like 1.0.4-3-ge1ca766 <- will not include the .dirty extension
export DISTANCE=$(echo $DESCRIBE | cut -d "-" -f 2)
export VERSION=$(echo $DESCRIBE | cut -d "-" -f 1)  # returns something like 1.0.4
#export VERSION=$(git describe --always --tags --first-parent)  # returns something like 1.0.4
if [ $DISTANCE -eq 0 ]; then
  pip install semver==2.13.0;  # does not need to be a package requirement as only needed when bumping up the version
  export VERSION=$(pysemver bump patch $VERSION).   # pysemver bumps  up the version number and tags it (unlike versioneer, which just adds the commits since the last tag)
  echo Bumping up version to $VERSION;
  git tag -a "$VERSION" -m "Release v. $VERSION";
  # You should do this again if you change the code/add tags/etc so it can update.
else
  echo No need to bump up version;
fi




echo Doing setup.py install
# Get list of commands by python setup.py --help-commands
python setup.py bdist_egg
#python setup.py install
#python setup.py sdist
#python setup.py bdist_wheel

#python -m pip install --upgrade build
#python -m build src/ --outdir dist/

echo Uploading to pypi/testpypi

python -m twine upload --repository testpypi dist/ryerrabelli-$VERSION*
#python -m twine upload --repository testpypi dist/*
#python -m twine upload dist/ryerrabelli-$VERSION*
#python -m twine upload dist/*

echo Done
