import unittest
import time


class TestImportTime(unittest.TestCase):
    # Cannot use "rsy.display_unittest_as_formatted" as ryerrabelli would already be imported then (even if you do
    # from ryerrabelli import display_unittest_as_formatted, the overall module is imported too- only the namespace
    # isn't copied over)
    def test_import(self):
        """
        This test function needs to be in a different file so that the module is not already loaded
        :return:
        :rtype:
        """
        tic = time.perf_counter()

        import ryerrabelli as my_module  # import to test time to import
        #import importlib
        #module_name = "ryerrabelli"
        #importlib.reload(module_name)

        toc = time.perf_counter()
        time_diff = toc-tic
        print(f"Import time: {time_diff} sec (for {my_module.__name__} version {my_module.__version__})")
        self.assertGreaterEqual(time_diff, 0)


if __name__ == '__main__':
    unittest.main()
