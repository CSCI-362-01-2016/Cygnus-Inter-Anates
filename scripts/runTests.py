import os, sys
import unittest

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
        self.failures.append((test, self._exc_info_to_string(err, test)))
        self._mirrorOutput = True
        self.tests_run.append([test.shortDescription(), self.testsRun, -1])

    def addSuccess(self, test):
        self.tests_run.append([test.shortDescription(), self.testsRun, 1])

class SetupTests():

    def __init__(self):
        self.importModules()

    def importModules(self):
        sys.path.append(os.path.join(os.path.dirname(__file__), "../testCasesExecutables"))
        sys.path.append(os.path.join(os.path.dirname(__file__), "../project/src"))
        importList =  os.listdir('../testCasesExecutables') + os.listdir('../project/src')
        for i in importList:
            if(i.endswith('.py')):
                moduleName = i[:-3]
                setattr(self, moduleName, __import__(moduleName))
        print self.music.noteToFreq(69)



    def run(self):
        suite = unittest.TestSuite()
        suite.addTest(getattr(getattr(self, 'testCase00'), 'TestNoteToFreq')('test', 'test1', 69, 440))
        result = CustomResults()
        suite.run(result)
        print result.getTestsReport()


if __name__ == '__main__':
    setupTests = SetupTests()
    setupTests.run()

    # for i in os.listdir('../testCasesExecutables/'):
    #     if(i.endswith('.py')):
    #         setattr(self, i[-3], __import__(i[-3]))
    #
    # suite = unittest.TestSuite()
    # suite.addTest(testCase00.TestNoteToFreq('test', "test1", 69, 440))
    # result = CustomResults()
    # suite.run(result)
    #
    # print
    # print result.getTestsReport()
