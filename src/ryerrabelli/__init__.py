"""ryerrabelli

Standard information / code to create a python project (specifically a package).

# To install the package in development (so can make changes while it is imported), run the below code
# pip install -e git+https://github.com/ryerrabelli/ryerrabelli.git#egg=ryerrabelli
"""

# Actions in "try:" happen when ryerrabelli module is used to set up any module besides ryerrabelli.
# Actions in "except:" happen when the ryerrabelli module is being setup itself, using the ryerrabelli module.
# Can't use the regular import statements when installing ryerrabelli bc ryerrabelli will not already be installed
# (duh), so can't import it, except by importing it as a relative path To keep the code the same, the renaming of the
# module(s) to "rsy" is helpful. However, for the relative import, we can only have one module named as rsy as we
# need one import statement per module (as opposed to one import statement for the entire package as done when
# ryerrabelli is used external code). Fortunately, each file that imports ryerrabelli only requires functions from
# one other module. The setup.py file only needs to import ryerrabelli functions that are in main.py (doesn't need
# any functions in utils.py) and main.py only needs to import functions from util.py
# ***NOTE: Above message is present in multiple files. Update text in all if comment is changed.
try:
    from ryerrabelli.packaging import *
    from ryerrabelli.constants import *
    from ryerrabelli.decorators import *
    # ryerrabelli.utils is not meant to be imported too - meant to have internal files only
except ImportError as e:
    from .packaging import *
    from .constants import *
    from .decorators import *
    # .utils is not meant to be imported too - meant to have internal files only


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions




