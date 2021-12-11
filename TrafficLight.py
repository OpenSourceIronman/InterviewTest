#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__company__ = "Loft Orbitial"
__status__  = "Development"
__date__    = "Late Updated: 2021-12-08"
__doc__     = "Simple traffic light object location and color instance variables"
"""

# Allow program to extract filename of the current file
# https://docs.python.org/3/library/os.html
import os

try:
    # Generate a timestamped .txt data logging file and custom terminal debugging output
    import Debug

    # Useful global constants used across all TesMuffler code
    import GlobalConstant as GC

except ImportError:
    print("Debug.py or GlobalConstant.py didn't import correctly")
    print("Please verify that those files are in same directory as the TrafficLight.py")


class TrafficLight:

    # Class variable to turn terminal and data logging print statements on and off
    DEBUG_STATEMENTS_ON = True

    def __init__(self, locationID, intersectionLocationIndex, initialColor=GC.RED):
        """[summary]

        Args:
            locationID ([INT]): [description]
            intersectionLocationIndex ([FLOAT]): [description]
            initialColor ([INT], optional): [description]. Defaults to GC.RED.
        """
        self.physicalLocation = locationID
        self.locationIndex = intersectionLocationIndex
        self.currentColor = initialColor

        thisCodesFilename = os.path.basename(__file__)
        self.DebugObject = Debug(TrafficLight.DEBUG_STATEMENTS_ON, thisCodesFilename)

    def turnGreen(self):
        self.currentColor = GC.GREEN

    def turnRed(self):
        self.currentColor = GC.RED
