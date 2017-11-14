import unittest
import HtmlTestRunner
import os
from searchmodule import SearchTests
from homepage import HomepageTest

result_dir = os.getcwd()

search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomepageTest)

smoke_tests = unittest.TestSuite([home_page_tests,search_tests])

outfile = open(result_dir + 'SomkeTestReport.html','w')

#runner = HtmlTestRunner.HTMLTestRunner(output = outfile)
runner = HtmlTestRunner.HTMLTestRunner(output='example_suite', report_title='My Report')

runner.run(smoke_tests)
