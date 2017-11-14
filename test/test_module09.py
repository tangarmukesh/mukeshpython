from mypackage.mymathlib import *
import unittest

math_obj = 0
def setUpModule():
    print("In setUpModule()...")
    global math_obj
    math_obj = mymathlib()

def tearDownModule():
    print("In tearDownModule()...")
    global math_obj
    del math_obj

class TestCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("In setUpClass()...")

    def setUp(self):
        print("In setUp()..")

    def test_case01(self):
        print("In test_case01")
        self.assertEqual(math_obj.add(2,3),5)

    def test_case02(self):
        print("In test_case02")

    def tearDown(self):
        print("In tearDown()...")

    @classmethod
    def tearDownClass(cls):
        print("In tearDownClass()..")
