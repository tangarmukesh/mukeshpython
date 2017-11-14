import unittest

def setUpModule():
    """called once,before anything else in this module"""
    print("In setUpModule()...")

def tearDownModule():
    """called once,after anything else in this module"""
    print("In tearDownModule()...")


class TestClass06(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """called once,before any test"""
        print("In setUpClass()...")

    @classmethod
    def tearDownClass(cls):
        """called once,after any test"""
        print("In tearDownClass()...")

    def setUp(self):
        """called multiple time,before every test method"""
        print("In setUp()...")

    def tearDown(self):
        """called multiple time,after every test method"""
        print("In tearDown()...")

    def test_case01(self):
        self.assertTrue("PYTHON".isupper())
        print("In test_case01()")

    def test_case02(self):
        self.assertTrue("python".islower())
        print("In test_case02()")

if __name__ == '__main__':
    unittest.main()
 
 
