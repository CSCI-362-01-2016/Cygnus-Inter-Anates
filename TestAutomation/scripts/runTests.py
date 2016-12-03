import os, sys
import unittest
import exceptions
sys.path.append(os.path.join(os.path.dirname(__file__), "../testCasesExecutables/"))
import jythonMusicTestCase


def parse():
    #Return 2D array [file][contents of file]
    fileContents = []
    for i in os.listdir('../testCases'):
        filename = str(i)
        f = open('../testCases/'+filename, 'r').read().splitlines()
        currentContents = []
        for line in f:
            currentContents.append(line)
        fileContents.append(currentContents)
    for i in range(len(fileContents)):
        #Evaluate input, keep the same if it is a string
        line2 = fileContents[i][2].split(" ")
        if len(line2) == 1:
            testModule = line2[0]
        else:
            testModule = line2[0]
            fileContents[i].append(line2[1])
        fileContents[i][2]
        try:
            testInput = eval('[' + fileContents[i][4] + ']')
        except:
            testInput = fileContents[i][4]
        fileContents[i][4] = testInput

        # equals, almostEquals
        if fileContents[i][5][:16] == 'testalmostequals':
            testType = ["testalmostequals",eval(fileContents[i][5][17:])]
        else:
            testType = [fileContents[i][5]]
        fileContents[i][5] = testType

        #Evaluate output, keep the same if it is a string
        try:
            testOutput = eval(fileContents[i][6])
            print str(testOutput)
            try:
                if isinstance(testOutput(), Exception):
                    testOutput = testOutput.__name__
            except:
                testOutput = testOutput
        except:
            testOutput = fileContents[i][6]
        fileContents[i][6] = testOutput

    return fileContents


class SetupTests():

    def __init__(self):
        self.fileContents = parse()

    def run(self):
        suite = unittest.TestSuite()
        for test in self.fileContents:
            test[5][0].lower()
            if len(test) == 7:
                suite.addTest(jythonMusicTestCase.JythonMusicTestCase(test[5], test[1], test[2], test[3], test[6], test[4], test[0]))
            else:
                suite.addTest(jythonMusicTestCase.JythonMusicTestCase(test[5], test[1], test[2], test[3], test[6], test[4], test[0], test[7]))
        reportFile = open('../reports/testReport.html', 'w')
        result = jythonMusicTestCase.CustomResults(reportFile, reportFile)
        suite.run(result)
        result.getHTMLReport()
        reportFile.close()
        sys.exit()

if __name__ == '__main__':
    setupTests = SetupTests()
    setupTests.run()
