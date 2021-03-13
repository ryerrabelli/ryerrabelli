# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
files = [file.lower() for file in os.listdir()]
if os.path.exists("docs"):
        files += [("docs" + os.sep + file.lower()) for file in os.listdir("docs")]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


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