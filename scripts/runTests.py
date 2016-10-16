import os, sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), "../testCasesExecutables"))

class CustomResults(unittest.TestResult):
    # code modified from http://code.activestate.com/recipes/578866-python-unittest-obtain-the-results-of-all-the-test/

    def __init__(self, stream=None, descriptions=None, verbosity=None):
        super(CustomResults, self).__init__()
        self._mirrorOutput = False
        self.tests_run = []

    def getTestsReport(self):
        return self.tests_run

    def addError(self, test, err):
        self.errors.append((test, self._exc_info_to_string(err, test)))
        self._mirrorOutput = True
        self.tests_run.append([test.shortDescription(), self.testsRun, 0])


    def addFailure(self, test, err):
        print 'failure'
        self.failures.append((test, self._exc_info_to_string(err, test)))
        self._mirrorOutput = True
        self.tests_run.append([test.shortDescription(), self.testsRun, -1])

    def addSuccess(self, test):
        self.tests_run.append([test.shortDescription(), self.testsRun, 1])

if __name__ == '__main__':

    testCase00 = __import__("testCase00")

    suite = unittest.TestSuite()
    suite.addTest(testCase00.TestNoteToFreq('test', "test1", 69, 440))
    result = CustomResults()
    suite.run(result)

    print
    print result.getTestsReport()
