import unittest
import time

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_import(self):
        tic = time.perf_counter()
        import ryerrabelli
        toc = time.perf_counter()
        print(f"Time: {toc} sec")


if __name__ == '__main__':
    unittest.main()
