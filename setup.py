"""
# Rahul Yerrabelli
# ryerrabelli@gmail.com
#
# Module setup file
# Originally created following this tutorial on versioning levels:
# https://jacobtomlinson.dev/posts/2020/creating-an-open-source-python-project-from-scratch/
# https://jacobtomlinson.dev/posts/2020/versioning-and-formatting-your-python-code/
"""

import setuptools
import os
import versioneer
from __init__ import get_module_data

#############################################
# BELOW LINE(S) MUST BE CHANGED FOR EVERY DIFFERENT PROJECT
module_name = "ryerrabelli"
#############################################

module_data = get_module_data(module_name=module_name)

print(module_data)
# Operator "**" unpacks dict into named arguments i.e. setup(name=x,version=y, cmdclass=z,...)
# Save it as a dict first so we can print it out
setuptools.setup(**module_data)

