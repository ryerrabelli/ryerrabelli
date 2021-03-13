"""
# Rahul Yerrabelli
#
# Module setup file
# Originally created following this tutorial on versioning levels:
# https://jacobtomlinson.dev/posts/2020/creating-an-open-source-python-project-from-scratch/
# https://jacobtomlinson.dev/posts/2020/versioning-and-formatting-your-python-code/
"""

import setuptools

import ryerrabelli as rsy


def setup():

    ####################################################################################################################
    # Below line needs to be changed for every different setup.py file
    module_name = "ryerrabelli"
    ####################################################################################################################


    # Originally, module_data is  outputted as a dict, which makes it easier for printing
    module_data = rsy.get_module_data(module_name=module_name)
    # Operator "**" unpacks dict into named arguments i.e. setup(name=x,version=y, cmdclass=z,...), which is
    # what setuptools.setup(.) requires
    print(module_data)
    setuptools.setup(**module_data)

if __name__ == '__main__':
    setup()
