import unittest
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../project/src"))
import music


class TestNoteToFreq(unittest.TestCase):

    def __init__(self, testname, description, midi, frequency):
        super(TestNoteToFreq, self).__init__(testname)
        self.description = description
        self.midi = midi
        self.frequency = frequency

    def test(self):
        """Test test test"""
        self.assertEqual(music.noteToFreq(self.midi), self.frequency)

    def shortDescription(self):
        return self.description

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
    if len(sys.argv) > 1:
        frequency = eval(sys.argv.pop())
        midi = eval(sys.argv.pop())
        description = sys.argv.pop()

    suite = unittest.TestSuite()
    suite.addTest(TestNoteToFreq('test', description, midi, frequency))
    suite.addTest(TestNoteToFreq('test', "testing2", 69, 440))
    suite.addTest(TestNoteToFreq('test', "testing3", 69, 441))
    result = CustomResults()
    suite.run(result)

    print
    print result.getTestsReport()

    #unittest.TextTestRunner(verbosity=2).run(suite)
