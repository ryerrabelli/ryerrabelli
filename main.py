# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, filenames, tool windows, actions, and settings.

import setuptools
import os

import versioneer

import utils
import ryerrabelli as rsy


if __name__ == '__main__':
    from _version import get_versions
    __version__ = get_versions()['version']
    del get_versions
    print(f"__version__ = {__version__}")



def get_var_from_file(file_choices,
                      func=lambda file: file.read(),
                      default=(None, None),
                      doc_folder="docs"):
    """
    case insensitive
    :param file_choices: Possible filenames for the variable of interest. Case insensitive.
    :type file_choices: list of str
    :param func: function applied to found file to get return value
    :type func: function
    :param default:
    :type default: tuple- 1st element matches expected return type or None, 2nd element filename (str) or None
    :param doc_folder: optional folder to additionally search for, beyond the root folder
    :type doc_folder: str
    :return: tuple of (func applied to the found file, filename of found file)
    :rtype: tuple of (type of func return, str)
    """
    def file_exists(path, use_list=True):
        return path.lower() in rsy.filenames if use_list else os.path.exists(path)
    for filename in file_choices:
        if file_exists(doc_folder + os.sep + filename):
            filename = doc_folder + os.sep + filename
        if file_exists(filename):
            with open(filename, "r") as file:
                return func(file), filename  # found a file, can now break
    return default


def extension_to_format(extension, default=""):
    """
    :param extension: file extension with or without the preceding . i.e. ".md", ".txt"
    :type extension: str
    :param default: default value to return if no description found
    :type default: str
    :return: description of extension type i.e. "text" or "text/markdown"
    :rtype: str
    """
    if extension.startswith("."):
        extension = extension[1:]
    if extension in ["", "txt", "text"]:
        return "text"
    elif extension in ["md"]:
        return "text/markdown"
    else:
        return default


#, path=os.path.abspath(os.curdir)
def get_module_data(module_name):
    """
    Note- this uses module os to get filenames from a relativ file path. Assuming that this is being run and imported by another program, the file path will be relative to the original program (as intended) and thus will use that python module's filenames (i.e. that module's LICENSE.txt, not this module's)


    :param module_name:
    :type module_name: str
    :return:
    :rtype: dict, need to apply ** operation (i.e. **returned_dict) before sending to setuptools.setup
    """
    # get_var_from_file(.) input is case insensitive, but most common case styles are shown for illustrative purposes
    if not rsy.long_descrip or not rsy.long_descrip_filename:
        rsy.long_descrip, rsy.long_descrip_filename \
            = get_var_from_file(["README", "README.txt", "README.md", "README.rs",
                                 "README-template", "README-template.txt",
                                 "README-template.md", "README-template.rs"],
                                lambda file: file.read(),  # Get string of text
                                default=("", None),
                                )
    if not rsy.requirements:
        rsy.requirements, _ \
            = get_var_from_file(["requirements", "requirements.txt"],
                                lambda file: [line.strip() for line in file],  # Get list of (str) requirements
                                default=([], None),
                                )
    if not rsy.license_text:
        # Can't name below variable license bc license() returns the python license
        rsy.license_text, _ \
            = get_var_from_file(["LICENSE", "LICENSE.txt", "LICENSE.md", "LICENSE.rtf"],
                                lambda file: file.read(),  # Get string of text
                                default=("", None),
                                )
    if not rsy.filenames:
        rsy.filenames = [file.lower() for file in os.listdir()]
        if os.path.exists("docs"):
            rsy.filenames += [("docs" + os.sep + file.lower()) for file in os.listdir("docs")]

    # For details on how to document, see:
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-py
    # Calls to versioneer are not to get versions of the ryerrabelli package, but to get the version of the original package.
    module_data = {
        "name": module_name,
        "version": versioneer.get_version(),  # str that includes git commit id per PEP format
        "cmdclass": versioneer.get_cmdclass(),
        "packages": setuptools.find_packages(),  # list, i.e. [""]
        "url": rsy.github_base + module_name,
        "license": rsy.license_text,
        "author": rsy.name,
        "author_email": rsy.name,
        "description": "",
        "install_requires": rsy.requirements,  # list of str
        "long_description": rsy.long_descrip,  # str
        "long_description_content_type":
            extension_to_format(rsy.long_descrip_filename.split("setup.py.")[-1]),
        "python_requires": ">=3.6",  # need python 3.6 or higher for f-strings
        "classifiers": [
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 3 - Alpha',

            # Indicate who your project is intended for
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',

            # Pick your license as you wish (should match "license" above)
            'License :: OSI Approved :: MIT License',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 3 :: Only',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            "Environment :: MacOS X"
            "Natural Language :: English"
            ],

    }
    print(module_data)
    # Operator "**" unpacks dict into named arguments i.e. setup(name=x,version=y, cmdclass=z,...)
    # Save it as a dict first so we can print it out
    return module_data

