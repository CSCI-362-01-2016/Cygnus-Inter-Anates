This is an automated testing framework for Jython Music, an open source music software.
Below are instructions on how to run the current tests, create new tests, create a new driver for a class function, and a walk through of how the automation works.

I. 	Run current tests available

	1. 	Navigate to the directory in the terminal using cd commands.
	2. 	Run the current tests with the command ./scripts/runAllTests.sh
		This will open an html when finished that displays whether tests have passed or failed.

II. Create new tests

	New tests must follow the following format:
		<test case id>
		<description of function's purpose>
		<module name> <class name if applicable>
		<function name>
		<input>
		<test type of expected output>
		<expected output>

	1. 	<test case id>
		The first line is a number representing a unique test case; the order does not affect the testing framework.
	2. 	<description of function's purpose>
		The second line is a description of what the function is expected to do, in brief detail.
	3.	<module name> <class name if applicable>
		The third line may consist of just a module name (if the method has no class, or a module name and a class. If a class is specified, there must be a driver built for the class method.  How to build a driver is discussed in detail in the next section.
	4.	<function name>
		The fourth line is the name of the function currently being tested.
	5.	<input>
		The fifth line is the input that is passed to the function for this particular test case
	6.	<test type of expected output>
		The sixth line specifies the test type, or the way that we are testing the function. If we want the output to match it exactly, or if we want it to be within a certain accuracy (this is used for floats with many trailing digits that we are not concerned about.)
		The two test types are:
			a.  testequals
				this test requires the expected output and actual output to match exactly
			b.	testalmostequals, <precision>
				this test requires the expected output to match the actual output, within <precision> decimal points.
	7.	<expected output>
		The seventh line specifies our expected output, or the type of exception if we are expecting an exception to be thrown.

III.Create a new driver for a class method

	Currently our framework only supports drivers for getter methods.
	The format "testCase_<class name>_<function name>.py" is used to name driver modules. Driver modules are placed in the testCasesExecutables folder.

	1.	At the top of the driver, add the project to the path using the code:

		import os,sys
		sys.path.append(os.path.join(os.path.dirname(__file__), "../project/src"))

	2. 	Import the module the class is located in.

		import <module name>

	3.	Create any complex variables that are needed beyond the test input to create an object of the class. These are variables that do not (or should not) affect the results of the test, but are too complex to be included directly in the creation of the class object, such as a function or an instance of another class object.

	4.	Create the test() function. Within the test function, create an instance of the class, named testClass, with the variables given by the test case input as well as any other variables required. Call the function being tested, <function name>, on the instance, and return the results.



IV.	Walk through of automation
