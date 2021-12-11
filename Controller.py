#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__company__ = "Loft Orbitial"
__status__  = "Development"
__date__    = "Late Updated: 2021-12-09"
__doc__     = "Control a 4-way traffic intersection with only RED-GREEN lights"
"""

# A lightweight, object-oriented Python state machine library
# https://pypi.org/project/transitions/
from transitions import Machine

# Define a system global clock
# https://docs.python.org/3/library/datetime.html#datetime.time
import time, datetime   # NOQA: E401

# Create random sensor events to simulate traffic
# https://docs.python.org/3/library/random.html
import random

# Allow program to extract filename of the current file
# https://docs.python.org/3/library/os.html
import os

# Allows for the creation of a GUI web app that communicates with python backend code
# Saves HTML files in a folder called "templates" in the same folder as your Flask code
# Saves user state / data across page refreshes and crashes, by using browser cookies
from flask import Flask, render_template, session

# Click on HTML table to update GUI / CSS classes
import pyautogui

try:
    # Generate a timestamped .txt data logging file and custom terminal debugging output
    import Debug

    # Two color (red & green) traffic light
    import TrafficLight

    # State Machine class with ?singelton? "pass"
    import Intersection

    # Useful global constants used across all classes
    import GlobalConstant as GC

except ImportError:
    print("Debug.py, TrafficLight.py, Intersectrion.py, or GlobalConstant.py didn't import correctly")
    print("Please verify that those files are in same directory as the Controller.py")

possibleStates = ['ALL_RED', 'NS_TURNING', 'NS_THROUGH', 'EW_TURNING', 'EW_THROUGH']

DEBUG_STATEMENTS_ON = True
TEST_MODE = False


def UnitTest():
    thisCodesFilename = os.path.basename(__file__)
    DebugObject = Debug(DEBUG_STATEMENTS_ON, thisCodesFilename)

    randomSensors = GetActiveVehicleSensors()
    DebugObject.Dprint(randomSensors)
    DebugObject.Lprint(GC.RED)


def GetActiveVehicleSensors():
    """ Update sensor List with random TRUE/FALSE items
        FALSE == 0 which means NO CAR IS ABOVE SENSOR

    Args:
        NONE

    Returns:
        [List]: [description]
    """
    sensors = [0] * GC.LANE_COUNT
    random.seed(datetime.datetime.now())

    for i in range(GC.LANE_COUNT):
        sensors[i] = random.randint(0, 1)

    return sensors


def UpdateTrafficLights(TrafficLightObjectList, nextState):
    """Update List of objects

    Args:
        TrafficLightObjectList ([type]): [description]
        nextState ([type]): [description]
    """
    if(nextState == 0):
        for i in range(1, GC.LANE_COUNT+1):
            TrafficLightObjectList[i].turnRed()
    if(nextState == 1):
        TrafficLightObjectList[GC.TL_SOUTHEAST_TURNINGLANE].turnGreen()
        TrafficLightObjectList[GC.TL_NORTHWEST_TURNINGLANE].turnGreen()
    if(nextState == 2):
        TrafficLightObjectList[GC.TL_SOUTHEAST_TURNINGLANE].turnRed()
        TrafficLightObjectList[GC.TL_NORTHWEST_TURNINGLANE].turnRed()

        TrafficLightObjectList[GC.TL_SOUTHSOUTH_THROUGHLANE].turnGreen()
        TrafficLightObjectList[GC.TL_NORTHNORTH_THROUGHLANE].turnGreen()
    if(nextState == 3):
        print("TODO")
    if(nextState == 4):
        print("TODO")


def main():
    # Define the 8 lane traffic light intersection outlined in take-home_pdf_specification.pdf
    TrafficLightObjectList = []
    for i in range(1, GC.LANE_COUNT+1):
        TrafficLightObjectList.append(TrafficLight(GC.USA_INTERSECTION_ID, i, GC.RED))   # NOQA: F405

    print("STARTING LOOP")
    startTime = time.time()  # seconds since January 1, 1970, 00:00:00 at UTC is epoch DONT use on 32-bit systems

    machine = Machine(model=Intersection.controlSystem, states=possibleStates, initial='ALL_RED')
    nextState = possibleStates[0]

    while():
        loopTime = (startTime - time.time()) % GC.MAX_CYCLE_TIME
        sensors = GetActiveVehicleSensors()

        if(not sensors[GC.TL_SOUTHEAST_TURNINGLANE] and not sensors[GC.TL_NORTHWEST_TURNINGLANE] or loopTime > GC.NS_TURNING_MAX):
            nextState = possibleStates[2]

        if(not sensors[GC.TL_SOUTHSOUTH_THROUGHLANE] and not sensors[GC.TL_NORTHNORTH_THROUGHLANE] or loopTime > GC.NS_THROUGH_MAX):
            nextState = possibleStates[3]

        if(not sensors[GC.TL_WESTSOUTH_TURNINGLANE] and not sensors[GC.TL_EASTNORTH_TURNINGLANE] or loopTime > GC.EW_TURNING_MAX):
            nextState = possibleStates[4]

        if(not sensors[GC.TL_WESTWEST_THROUGHLANE] and not sensors[GC.TL_EASTEAST_THROUGHLANE] or loopTime > GC.EW_THROUGH_MAX):
            nextState = possibleStates[1]

        UpdateTrafficLights(TrafficLightObjectList, nextState)

        time.sleep(0.5) # Make while loop last 1 second

if __name__ == "__main__":
    if(TEST_MODE):
        UnitTest()
    else:
        main()
