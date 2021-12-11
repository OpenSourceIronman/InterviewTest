#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__company__ = "Loft Orbital"
__status__  = "Development"
__date__    = "Late Updated: 2021-12-08"
__doc__     = "Useful global constants used for traffic light control"
"""

# Traffic light color CONTSTANTS
RED = 0
GREEN = 1

# Traffic sensor color CONSTANTS
ORANGE = 1
WHITE = 0

# Traffic light ID & Lane CONTSTANTS
# One of 330,000 traffic lights in the USA at GPS location 36.04118372490759, -115.25226103355224
# Each lane is identified by it's ENTER and EXIT cardinal directions
# Not optimized for program size but easy of implementation
# TODO Implement as python dictionary imported from CSV file
USA_INTERSECTION_ID = 42000
TL_SOUTHSOUTH_THROUGHLANE = 1
TL_SOUTHEAST_TURNINGLANE = 2
TL_WESTWEST_THROUGHLANE = 3
TL_WESTSOUTH_TURNINGLANE = 4
TL_NORTHNORTH_THROUGHLANE = 5
TL_NORTHWEST_TURNINGLANE = 6
TL_EASTEAST_THROUGHLANE = 7
TL_EASTNORTH_TURNINGLANE = 8
LANE_COUNT = 8

# Min and max active times for lights (Table #1 in take-home_pdf_specifications.pdf) - Units are seconds
NS_TURNING_MIN = 10.0
NS_TURNING_MAX = 60.0
NS_THROUGH_MIN = 30.0
NS_THROUGH_MAX = 120.0
EW_TURNING_MIN = 10.0
EW_TURNING_MAX = 30.0
EW_THROUGH_MIN = 30.0
EW_THROUGH_MAX = 60.0
MAX_CYCLE_TIME = NS_TURNING_MAX + NS_THROUGH_MAX + EW_TURNING_MAX + EW_THROUGH_MAX

# User Interface timing CONSTANTS
UI_TERMINAL_DELAY = 0.01                # Units are seconds
MAX_UI_DEALY = 2.0                      # Units are seconds
CPU_DELAY = 5.0                         # Units are milliSeconds


class GlobalConstant:

    def unitTest():
        assert UI_TERMINAL_DELAY < 0.02
        assert int(GlobalConstant.TL_SOUTHSOUTH_THROUGHLANE) == USA_INTERSECTION_ID
        assert RED == 0
        assert NS_TURNING_MIN > 9.5, "Unit Test passed successfully"


if __name__ == "__main__":
    print("Starting GlobalConstant.py unitTest()")
    GlobalConstant.unitTest()
