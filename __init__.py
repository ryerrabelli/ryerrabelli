import setuptools
import os
import versioneer

from main import *


def get_module_data(module_name = "YerrabelliFlask"):
    # get_var_from_file(.) input is case insensitive, but most common case styles are shown for illustrative purposes
    long_descrip, long_descrip_filename \
        = get_var_from_file(["README", "README.txt", "README.md", "README.rs",
                             "README-template", "README-template.txt",
                             "README-template.md", "README-template.rs"],
                            lambda file: file.read(),  # Get string of text
                            default=("", None),
                            )
    requirements, _ = get_var_from_file(["requirements", "requirements.txt"],
                                        lambda file: [line.strip() for line in file],  # Get list of (str) requirements
                                        default=([], None),
                                        )
    # Can't name below variable license bc license() returns the python license
    license_text, _ = get_var_from_file(["LICENSE", "LICENSE.txt", "LICENSE.md", "LICENSE.rtf"],
                                        lambda file: file.read(),  # Get string of text
                                        default=("", None),
                                        )
    # For details on how to document, see:
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-py
    module_data = {
        "name": module_name,
        "version": versioneer.get_version(),  # str that includes git commit id per PEP format
        "cmdclass": versioneer.get_cmdclass(),
        "packages": setuptools.find_packages(),  # list, i.e. [""]
        "url": "https://github.com/ryerrabelli/" + module_name,
        "license": license_text,
        "author": "Rahul Yerrabelli",
        "author_email": "ryerrabelli@gmail.com",
        "description": "",
        "install_requires": requirements,  # list of str
        "long_description": long_descrip,  # str
        "long_description_content_type": extension_to_format(long_descrip_filename.split("setup.py.")[-1]),
    }
    print(module_data)
    # Operator "**" unpacks dict into named arguments i.e. setup(name=x,version=y, cmdclass=z,...)
    # Save it as a dict first so we can print it out
    return module_data


if __name__ == '__main__':
    pass
    #main()

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
