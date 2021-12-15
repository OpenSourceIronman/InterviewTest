WARNING: On MacOS 12.0.1 I had to install WxPython on my whole system using "pip3 install wxpython" outside any VirtualEnv to bypass some black screen issues <br>

VirtualEnv was used to create an isolated Python environment. Since Python 3.3 a subset of VirtualEnv has been integrated into the standard library (See https://virtualenv.pypa.io/en/latest/). The necessary virtual environment can be configured on your system by using the terminal command "source LoftOrbitalDevEnv/bin/activate" while in the "InterviewTest" directory, or by running the terminal command "pip3 install transitions" which will install the only needed dependency on your system. <br>

Controller.py is the entry point for this code demo and should be run using the terminal command "python3 Controller.py" <br>

The UnitTest() function is invoked by setting the following CONSTANSTS in Controller.py (See line 69) <br>
1. UNIT_TEST_MODE = True
2. DEBUG_STATEMENTS_ON = True
3. Passing the desired interger testCase (1, 2, or 3) on line 228 of Controller.py  

The high level State Machine is defined by the Controller.py GLOBAL variables *possibleStates* and *trafficFlowTransitions*

This test required ~538 lines of code to complete

Code was linted using Flake8 with custom 135 line lengths 

Future Work (See GUI-Dev branch of this repo):
1. In GlobalConstants.py implement "Traffic light ID & Lane CONTSTANTS" definition via CSV file import
2. Finish Flask GUI update by passing sensor and traffic light Lists to render_temple() function to change CSS
