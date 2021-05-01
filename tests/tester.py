import unittest
import time
import pprint


class MyTestCase(unittest.TestCase):
    def test_import(self):
        tic = time.perf_counter()
        import ryerrabelli as my_module  # import to test time to import
        toc = time.perf_counter()
        time_diff = toc-tic
        print(f"Import time: {time_diff} sec (for {my_module.__name__} version {my_module.__version__})")
        self.assertGreaterEqual(time_diff, 0)

    def test_variables(self):
        import ryerrabelli as rsy
        #print(rsy.__dict__)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(rsy.__dict__)




if __name__ == '__main__':
    unittest.main()
