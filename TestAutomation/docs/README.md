# Getting Started with JythonMusic TestAutomation

This is an automated testing framework for Jython Music, an open source music software.
Below are instructions on how to run the current tests, create new tests, create a new driver for a class function, and a walk through of how the automation works.


##Run current tests available

1. Navigate to the TestAutomation directory in the terminal.
2. Run the current tests with the command ./scripts/runAllTests.sh
3. This will open your default browser with an HTML page of the results


##Create new tests

New tests must follow the following format:

    <test case id>
    <description of function's purpose>
    <module name> <class name if applicable>
    <function name>
    <input>
    <test type of expected output>
    <expected output>

###\<test case id>

The first line is a number representing a unique test case; the order does not affect the testing framework.


###\<description of function's purpose>

The second line is a description of what the function is expected to do, in brief detail.


###\<module name> \<class name if applicable>

The third line may consist of just a module name (if the method has no class, or a module name and a class. If a class is specified, there must be a driver built for the class method.  How to build a driver is discussed in detail in the next section.


###\<function name>

The fourth line is the name of the function currently being tested.


###\<input>

The fifth line is the input that is passed to the function for this particular test case


###\<test type of expected output>

The sixth line specifies the test type, or the way that we are testing the function. If we want the output to match it exactly, or if we want it to be within a certain accuracy (this is used for floats with many trailing digits that we are not concerned about.)

The two test types are:

* testequals - this test requires the expected output and actual output to match exactly
* testalmostequals, \<precision> - this test requires the expected output to match the actual output, within \<precision> decimal points.


###\<expected output>

The seventh line specifies our expected output, or the type of exception if we are expecting an exception to be thrown.


##Create a new driver for a class method

Currently our framework only supports drivers for getter methods.
The format "testCase_\<class name>_\<function name>.py" is used to name driver modules. Driver modules are placed in the testCasesExecutables folder.

1. At the top of the driver, add the project to the path using the code:
    
    ```
    import os,sys
    sys.path.append(os.path.join(os.path.dirname(__file__), "../project/src"))
    ```
    
2. Import the module the class is located in.
    
    ```
    import \<module name>
    ```
3. Create any complex variables that are needed beyond the test input to create an object of the class. These are variables that do not (or should not) affect the results of the test, but are too complex to be included directly in the creation of the class object, such as a function or an instance of another class object.

4. Create the test() function. Within the test function, create an instance of the class, named testClass, with the variables given by the test case input as well as any other variables required. Call the function being tested, \<function name>, on the instance, and return the results.


##Walk through of automation

Once all of your test cases are created, you can run the test automation framework with the ./scripts/runAllTests.sh script. All of the test cases are automatically generated from the test case text files listed in the ./testCases directory. It then iterates through the tests, running each one and then opening a browser with an HTML page of the results.

###How it works

####SetupTests

The first thing that happens when the automation framework is run, is SetupTests is initialized. This initialization includes parsing the testCase text files in the ./testCases directory. SetupTests has a run method which begins by creating a Python TestSuite object. Then it takes the data previously parsed from ./testCases, creates an instance of JythonMusicTestCase for each, and passes them all into the TestSuite object. After the TestSuite is populated, SetupTests creates a CustomResults object and calls TestSuite.run(CustomResults). This runs the automation. Finally SetupTests opens the browser with an HTML page of the results.

####JythonMusicTestCase

An instance of JythonMusicTestCase is created for each of the text files in the ./testCases directory. JythonMusicTestCase is a child of Python's TestCase class. It contains the logic for any method that is scoped to a module, however it needs class specific drivers in order to test methods within classes. As with any of Python's TestClass objects, JythonMusicTestCase can be run independently of a suite by simply calling JythonMusicTestCase.run(TestResults). You could even input your own implementation of the TestResults object: JythonMusicTestCase.run(MyTestResults).

####CustomResults

CustomResults contains all of the logic for creating an HTML document from the test results. Throughout the lifecycle of TestSuite's run method, CustomResults appends the results of each of the JythonMusicTestCases. After the suite is finished SetupTests calls CustomResult's getHTMLReport method which uses Python templating to write to an HTML document in ./reports/testReport.html.
