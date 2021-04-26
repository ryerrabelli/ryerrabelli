from functools import wraps
import time

# All the below variables are defined so they are accessible from the ryerrabelli module
first_name = "Rahul"
last_name = "Yerrabelli"
middle_initial = "S"
name = first_name + last_name
emails = {}
emails["gmail"] = default_email = email = gmail = "ryerrabelli+python@gmail.com"
username = handle = "ryerrabelli"
github_base = "https://github.com/ryerrabelli/"

long_descrip = None
long_descrip_filename = None
requirements = None
license_text = None

filenames = None



def analyze_function(print_args: bool = True, time_fmt: str = "0.4f", do: bool =True, is_command: bool = True):
    """This is a decorator function used to nicely time functions as well as print out their inputs.
    # https://stackoverflow.com/questions/52214720/whether-the-return-value-of-a-function-modified-by-python-decorator-can-only-be
    # https://www.geeksforgeeks.org/decorator-to-print-function-call-details-in-python/
    The arguments to the outer "analyze_function(.)" function are arguments to the decorator (like @analyze_function(do=False) )
    :param print_args:
    :type print_args: bool
    :param time_fmt: format of time
    :type time_fmt: str
    :param do: Making this false is the same as not calling this function. Having it as a variable makes the syntax sometimes easier.
    :type do: bool
    :param is_command: The is_commands variable is for functions like "run_command(commands, args,...)" where commands=["git"] and args=["describe","--tags"] so that the output into bash/zsh is like "git describe --tags"
    :type is_command: bool
    :return:
    :rtype:
    """

    def decorator(func):
        """

        :param func: The function being wrapped. The "@" syntactic sugar automatically puts this as an argument.
        :type func: function
        :return:
        :rtype:
        """
        # Getting the argument names of the called function
        arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]

        @wraps(func)
        def wrapper(*args, **kwargs):
            """

            :param args: the positional arguments to the decorated function
            :type args: list
            :param kwargs: the named arguments to the decorated function
            :type kwargs: list
            :return: same as the decorated function
            :rtype: same as the decorated function
            """
            if not do:
                return func(*args, **kwargs)

            if is_command:
                print(" ".join([" ".join(args[0])] + args[1]))

            t0 = time.time()
            try:
                return func(*args, **kwargs)
            finally:  # "finally" runs no matter what - whether error is thrown or not, even if return keyword is given
                t1 = time.time()
                # There also is the func.__code__ var, but that is too much to print nicely
                if print_args:
                    # print(f"Took {t1 - t0:{time_fmt}} sec to run: {func.__name__}({', '.join('% s = % r' % entry for entry in zip(argnames, args[:len(argnames)]))} ), args = {list(args[len(argnames):])}, kwargs = {kwargs}")
                    print(f"Took {t1 - t0:{time_fmt}} sec to run: {func.__name__}" +
                          f"({', '.join('% s=% r' % entry for entry in zip(arg_names, args[:len(arg_names)]))} ), args = {list(args[len(arg_names):])}, kwargs = {kwargs}")
                else:
                    print(f"Took {t1 - t0:{time_fmt}} sec to run '{func.__name__}'")

        return wrapper

    return decorator
