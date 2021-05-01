import unittest
import pprint
import ryerrabelli as rsy


class MyTestCase(unittest.TestCase):
    @rsy.display_unittest_as_formatted
    def test_variables(self):
        import ryerrabelli as rsy
        #print(rsy.__dict__)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(rsy.__dict__)




if __name__ == '__main__':
    unittest.main()
