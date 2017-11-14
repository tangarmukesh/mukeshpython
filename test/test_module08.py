import unittest
import test_me

class TestClass09(unittest.TestCase):

    def test_case01(self):
        self.assertEqual(test_me.add(2,3),5)
        print("In test_case01()")
