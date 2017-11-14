import unittest
from searchmodule import SearchTests
from homepage import HomepageTest

search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomepageTest)

smoke_tests = unittest.TestSuite([home_page_tests,search_tests])

unittest.TextTestRunner(verbosity=2).run(smoke_tests)
