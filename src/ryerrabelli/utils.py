first_name = "Rahul"
last_name = "Yerrabelli"
middle_initial = "S"
name = first_name + last_name
emails = {}
emails["gmail"] = default_email = email = gmail = "ryerrabelli+python@gmail.com"
username = handle = "ryerrabelli"
github_base = ""

long_descrip = None
long_descrip_filename = None
requirements = None
license_text = None

filenames = None



# https://stackoverflow.com/questions/52214720/whether-the-return-value-of-a-function-modified-by-python-decorator-can-only-be
# https://www.geeksforgeeks.org/decorator-to-print-function-call-details-in-python/
from functools import wraps
import time
def timer(func, print_args=True, fmt="0.4f"):
    # Getting the argument names of the
    # called function
    argnames = func.__code__.co_varnames[:func.__code__.co_argcount]

    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        try:
            return func(*args, **kwargs)
        finally:  # Finally runs no matter what - whether error is thrown or not, even if return keyword is given
            t1 = time.time()
            # There also is the func.__code__ var, but that is too much to print nicely
            if print_args:
                #print(f"Took {t1 - t0:{fmt}} sec to run: {func.__name__}({', '.join('% s = % r' % entry for entry in zip(argnames, args[:len(argnames)]))} ), args = {list(args[len(argnames):])}, kwargs = {kwargs}")
                print(f"Took {t1 - t0:{fmt}} sec to run: {func.__name__}" +
                      f"({', '.join('% s=% r' % entry for entry in zip(argnames, args[:len(argnames)]))} ), args = {list(args[len(argnames):])}, kwargs = {kwargs}")
            else:
                print(f"Took {t1 - t0:{fmt}} sec to run '{func.__name__}'")
    return wrapper