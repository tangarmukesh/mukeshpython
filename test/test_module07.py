import unittest

class TestClass08(unittest.TestCase):

    def test_case01(self):
        self.assertTrue("PYTHON".isupper())
        print("In test_case1()")

    def test_case02(self):
        self.assertTrue("PYTHON".islower())
        print("In test_case2()")

    def test_case03(self):
        self.assertTrue(True)
        print("In test_case3()")
