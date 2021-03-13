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


#############################################
# BELOW LINE(S) MUST BE CHANGED FOR EVERY DIFFERENT PROJECT
module_name = "YerrabelliFlask"
#############################################


# Search through all files instead of os.path.exists so it is case insensitive regardless of the file system
files = [file.lower() for file in os.listdir()] + \
        [("docs" + os.sep + file.lower()) for file in os.listdir("docs") if os.path.exists("docs")]


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
        return path.lower() in files if use_list else os.path.exists(path)
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

# get_var_from_file(.) input is case insensitive, but most common case styles are shown for illustrative purposes
long_descrip, long_descrip_filename \
                = get_var_from_file(["README", "README.txt", "README.md", "README.rs",
                                     "README-template", "README-template.txt",
                                     "README-template.md", "README-template.rs"],
                                    lambda file: file.read(),                      # Get string of text
                                    default=("",None),
                                    )
requirements, _ = get_var_from_file(["requirements", "requirements.txt"],
                                    lambda file: [line.strip() for line in file],  # Get list of (str) requirements
                                    default=([],None),
                                    )
# Can't name below variable license bc license() returns the python license
license_text, _ = get_var_from_file(["LICENSE", "LICENSE.txt", "LICENSE.md", "LICENSE.rtf"],
                                    lambda file: file.read(),                      # Get string of text
                                    default=("",None),
                                    )
# For details on how to document, see:
# https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-py
module_data = {
    "name":                          module_name,
    "version":                       versioneer.get_version(),      # str that includes git commit id per PEP format
    "cmdclass":                      versioneer.get_cmdclass(),
    "packages":                      setuptools.find_packages(),    # list, i.e. [""]
    "url":                           "https://github.com/ryerrabelli/" + module_name,
    "license":                       license_text,
    "author":                        "Rahul Yerrabelli",
    "author_email":                  "ryerrabelli@gmail.com",
    "description":                   "",
    "install_requires":              requirements,                  # list of str
    "long_description":              long_descrip,                  # str
    "long_description_content_type": extension_to_format(long_descrip_filename.split(".")[-1]),
}
print(module_data)
# Operator "**" unpacks dict into named arguments i.e. setup(name=x,version=y, cmdclass=z,...)
# Save it as a dict first so we can print it out
setuptools.setup(**module_data)

