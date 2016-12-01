import unittest
import os, sys
from types import *
class Template:

    def __init__(self, template, dict):
        self.template = template
        self.dict = dict

    def __str__(self):
        return self.template % self.dict

class CustomResults(unittest.TestResult):
    # code modified from http://code.activestate.com/recipes/578866-python-unittest-obtain-the-results-of-all-the-test/

    def __init__(self, stream=None, descriptions=None, verbosity=None):
        super(CustomResults, self).__init__()
        self._mirrorOutput = False
        self.tests_run = []
        self.stream = stream

    def getTestsReport(self):
        self.tests_run = sorted(self.tests_run, key=lambda k: k['testNumber'])
        return self.tests_run

    def getHTMLReport(self):
        rowTemplate = """
        <tr>
            <td>%(testNumber)s</td>
            <td>%(testDescription)s</td>
            <td>%(testModule)s</td>
            <td>%(testFunction)s</td>
            <td>%(testName)s</td>
            <td>%(inputs)s</td>
            <td>%(expected)s</td>
            <td>%(actual)s</td>
            <td class="%(success)s">%(success)s</td>
        </tr>
        """

        documentTemplate = """
        <html>
            <head>
                <title>Test Results</title>
                <link rel="stylesheet" href="styles.css"/>
            </head>
            <body>
                <table>
                    <tr>
                        <th>Number</th>
                        <th>Description</th>
                        <th>Module</th>
                        <th>Function</th>
                        <th>Type</th>
                        <th>Inputs</th>
                        <th>Expected</th>
                        <th>Actual</th>
                    </tr>
                    %(resultRows)s
                </table>
            </body>
        </html>
        """
        rowAccumulator = ''
        for test in self.getTestsReport():
            rowAccumulator += Template(rowTemplate, test).__str__()
        self.stream.write(Template(documentTemplate, {'resultRows': rowAccumulator}).__str__())

    def addError(self, test, err):
        self.errors.append((test, self._exc_info_to_string(err, test)))
        self._mirrorOutput = True
        info = test.getTestInformation()
        info['success'] = 'error'
        self.tests_run.append(info)

    def addFailure(self, test, err):
        self.failures.append((test, self._exc_info_to_string(err, test)))
        self._mirrorOutput = True
        info = test.getTestInformation()
        info['success'] = 'fail'
        self.tests_run.append(info)

    def addSuccess(self, test):
        info = test.getTestInformation()
        info['success'] = 'success'
        self.tests_run.append(info)


def initializeGeneralClass(base):
    class GeneralClass(base):

        def __init__(self, initArgs):
            super(GeneralClass, self).__init__(*initArgs)

        def test(self):
            attrDict = {}
            for key in dir(self):
                if(hasattr(self, key)) and (not isinstance(getattr(self, key), FunctionType) and key == 'test'):
                    print key + ": " + `getattr(self,key)`
                    attrDict[key] = getattr(self,key)
            return attrDict

        def __eq__(self,other):
            if instance(other, self.__class__):
                return self.__dict__ == other.__dict__

        def __ne__(self, other):
            return not self.__eq__(other)


    return GeneralClass


class JythonMusicTestCase(unittest.TestCase):

    def __init__(self, testname, description, testModule, testFunction, outputValue, inputs, testNumber=None, testClass = None):
        super(JythonMusicTestCase, self).__init__(testname[0])
        self.testname = testname[0]
        self.description = description
        self.inputs = inputs
        self.testModule = testModule
        self.testFunction = testFunction
        self.outputValue = outputValue
        self.testNumber = testNumber
        self.testClass = testClass
        if testname[0] == "testalmostequals":
            self.testalmostequalsprecison = testname[1]
        self.importModules()
        # if self.testModule == 'music':
        #     TestNoteClass = initializeGeneralClass(getattr(self, self.testModule).Note)
        #     testNoteObj = TestNoteClass([getattr(self, self.testModule).A4, 4.0])
        #     print testNoteObj.test()
        if self.testClass == None:
            try:
                self.actualResults = getattr(getattr(self, self.testModule), self.testFunction)(*self.inputs)
            except Exception, e:
                self.actualResults = type(e).__name__
        else:
            self.executableName = "testCase_" + str(testClass) + "_" + str(testFunction)
            setattr(self, self.executableName, __import__(self.executableName))
            try:
                self.actualResults = getattr(self, self.executableName).test(*self.inputs)
            except Exception, e:
                self.actualResults = type(e).__name__

    def importModules(self):
        sys.path.append(os.path.join(os.path.dirname(__file__), "../project/src"))
        importList = os.listdir('../project/src')
        for i in importList:
            if(i.endswith('.py')):
                moduleName = i[:-3]
                setattr(self, moduleName, __import__(moduleName))

    def testequals(self):
        self.assertEqual(self.actualResults, self.outputValue)

    def testalmostequals(self):
        self.assertAlmostEqual(self.actualResults, self.outputValue, self.testalmostequalsprecison) #Allow tester to set precision

    def shortDescription(self):
        return self.description

    def getTestInformation(self):
        return {
        'testNumber': self.testNumber,
        'testDescription': self.description,
        'testModule': self.testModule,
        'testFunction': self.testFunction,
        'testName': self.testname,
        'inputs': self.inputs,
        'expected': self.outputValue,
        'actual': self.actualResults
        }


if __name__ == '__main__':
    if len(sys.argv) > 1:
        inputs = eval('[' + sys.argv.pop() + ']')
        outputValue = eval(sys.argv.pop())
        testFunction = sys.argv.pop()
        testModule = sys.argv.pop()
        description = sys.argv.pop()
        testName = sys.argv.pop()

    result = CustomResults()
    test = JythonMusicTestCase(testName, description, testModule, testFunction, outputValue, inputs)
    test.run(result)
    print
    print result.getTestsReport()[0]
    sys.exit()
