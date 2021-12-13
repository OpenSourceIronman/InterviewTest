#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__company__ = "Loft Orbitial"
__status__  = "Development"
__date__    = "Late Updated: 2021-12-12"
__doc__     = "Control a 4-way traffic intersection with 8 RED-GREEN lights"
__link__    = https://github.com/OpenSourceIronman/InterviewTest
"""

# A lightweight, object-oriented Python state machine library
# https://pypi.org/project/transitions/
from transitions import Machine, State

# Pause program execution and elect seed for pseudo random generator
# https://docs.python.org/3/library/datetime.html#datetime.time
import time
import datetime

# Create random sensor events to simulate traffic
# https://docs.python.org/3/library/random.html
import random

# Allow program to extract filename of the current file
# https://docs.python.org/3/library/os.html
import os


try:
    # Generate a timestamped .txt data logging file and custom terminal debugging output
    import Debug as Debug

    # Two color (red & green) traffic light
    import TrafficLight as TL

    # State Machine class with ?singelton? "pass"
    import Intersection as Intersection

    # Useful global constants used across all classes
    import GlobalConstant as GC

except ImportError:
    print("Debug.py, TrafficLight.py, Intersectrion.py, or GlobalConstant.py didn't import correctly")
    print("Please verify that those files are in same directory as the Controller.py")

# Global variables of Controller.py that define the overall State Machine
possibleStates = [State(name='ALL_RED'),
                  State(name='NS_TURNING'), State(name='NS_THROUGH'),
                  State(name='EW_TURNING'), State(name='EW_THROUGH')]

trafficFlowTransitions = [
    {'trigger': 'ALLOW_NS_TURNING', 'source': 'EW_THROUGH', 'dest': 'NS_TURNING'},
    {'trigger': 'NS_THROUGH_ONLY', 'source': 'NS_TURNING', 'dest': 'NS_THROUGH'},
    {'trigger': 'ALLOW_EW_TURNING', 'source': 'NS_THROUGH', 'dest': 'EW_TURNING'},
    {'trigger': 'EW_THROUGH_ONLY', 'source': 'EW_TURNING', 'dest': 'EW_THROUGH'},

    {'trigger': 'emergencyStop', 'source': 'NS_TURNING', 'dest': 'ALL_RED'},
    {'trigger': 'emergencyStop', 'source': 'NS_THROUGH', 'dest': 'ALL_RED'},
    {'trigger': 'emergencyStop', 'source': 'EW_TURNING', 'dest': 'ALL_RED'},
    {'trigger': 'emergencyStop', 'source': 'EW_THROUGH', 'dest': 'ALL_RED'},

    {'trigger': 'start', 'source': 'ALL_RED', 'dest': 'EW_THROUGH'},
]


# Global "CONSTANTS" to Controller.py
TIME_STEP = 5
UNIT_TEST_MODE = False
DEBUG_STATEMENTS_ON = True
THIS_CODES_FILENAME = os.path.basename(__file__)

DebugObject = Debug.Debug(DEBUG_STATEMENTS_ON, THIS_CODES_FILENAME)


def UnitTest(testCase):
    """Update this function to test new edge cases

    Args:
        testCase (INTEGER): Discrete test number to run
    """

    if(testCase == 1):
        randomSensors = GetActiveVehicleSensors()
        DebugObject.Dprint(randomSensors)
    elif(testCase == 2):
        TrafficLightObjectList = TL.TrafficLight(GC.USA_INTERSECTION_ID, 1, GC.GREEN)
        TrafficLightObjectList.append(TL.TrafficLight(GC.USA_INTERSECTION_ID, 2, GC.RED))
        UpdateTrafficLights(TrafficLightObjectList, possibleStates[1])
        DebugObject.Dprint(TrafficLightObjectList.currentColor)
    elif(testCase == 3):
        print("TODO")
        assert GC.RED == 0


def GetActiveVehicleSensors():
    """ Update sensor List with random TRUE/FALSE items to simulate traffic flow
        FALSE == 0 which means NO CAR IS ABOVE SENSOR

    Args:
        NONE

    Returns:
        [List]: New random sensors List
    """
    sensors = [0] * GC.LANE_COUNT
    random.seed(datetime.datetime.now())

    for i in range(GC.LANE_COUNT):
        sensors[i] = random.randint(0, 1)

    # TODO: Intersection.GUI_Update(GC.SENSORS_GUI, sensors)
    return sensors


def UpdateTrafficLights(TrafficLightObjectList, controlSystem, prevState):
    """Update TrafficLight Objects

    Args:
        TrafficLightObjectList (List): [description]
        controlSystem (Intersection Object)
        nextState (List): [description]
    """

    if(controlSystem.state == 'ALL_RED'):
        for i in range(GC.LANE_COUNT):
            TrafficLightObjectList[i].turnRed()

    if(controlSystem.state == 'NS_TURNING'):
        for i in range(GC.LANE_COUNT):
            TrafficLightObjectList[i].turnRed()
        time.sleep(GC.RED_TO_GREEN_SAFETY_DELAY)
        TrafficLightObjectList[GC.TL_SOUTHEAST_TURNINGLANE].turnGreen()
        TrafficLightObjectList[GC.TL_NORTHWEST_TURNINGLANE].turnGreen()

    if(controlSystem.state == 'NS_THROUGH'):
        for i in range(GC.LANE_COUNT):
            TrafficLightObjectList[i].turnRed()
        time.sleep(GC.RED_TO_GREEN_SAFETY_DELAY)
        TrafficLightObjectList[GC.TL_SOUTHSOUTH_THROUGHLANE].turnGreen()
        TrafficLightObjectList[GC.TL_NORTHNORTH_THROUGHLANE].turnGreen()

    if(controlSystem.state == 'EW_TURNING'):
        for i in range(GC.LANE_COUNT):
            TrafficLightObjectList[i].turnRed()
        time.sleep(GC.RED_TO_GREEN_SAFETY_DELAY)
        TrafficLightObjectList[GC.TL_WESTSOUTH_TURNINGLANE].turnGreen()
        TrafficLightObjectList[GC.TL_EASTNORTH_TURNINGLANE].turnGreen()

    if(controlSystem.state == 'EW_THROUGH'):
        for i in range(GC.LANE_COUNT):
            TrafficLightObjectList[i].turnRed()
        time.sleep(GC.RED_TO_GREEN_SAFETY_DELAY)
        TrafficLightObjectList[GC.TL_WESTWEST_THROUGHLANE].turnGreen()
        TrafficLightObjectList[GC.TL_EASTEAST_THROUGHLANE].turnGreen()

    if(prevState != controlSystem.state):
        print("STATE = " + str(controlSystem.state))
        for i in range(GC.LANE_COUNT):
            print("TRAFFIC LIGHT # = ", i, " is " + str(TrafficLightObjectList[i].getColor()))

        # TODO: Intersection.GUI_Update(GC.TRAFFIC_LIGHT_GUI, TrafficLightObjectList)
        print("\n\n")


def Main():
    DebugObject = Debug.Debug(DEBUG_STATEMENTS_ON, THIS_CODES_FILENAME)

    # Define 8 lane traffic light intersection with inital state outlined in take-home_pdf_specification.pdf
    TrafficLightObjectList = [TL.TrafficLight(GC.NULL_ID, GC.NULL_INDEX, GC.RED)] * 8

    TrafficLightObjectList[0] = TL.TrafficLight(GC.USA_INTERSECTION_ID, GC.TL_SOUTHSOUTH_THROUGHLANE, GC.RED)
    TrafficLightObjectList[1] = TL.TrafficLight(GC.USA_INTERSECTION_ID, GC.TL_SOUTHEAST_TURNINGLANE, GC.RED)
    TrafficLightObjectList[2] = TL.TrafficLight(GC.USA_INTERSECTION_ID, GC.TL_WESTWEST_THROUGHLANE, GC.GREEN)
    TrafficLightObjectList[3] = TL.TrafficLight(GC.USA_INTERSECTION_ID, GC.TL_WESTSOUTH_TURNINGLANE, GC.RED)
    TrafficLightObjectList[4] = TL.TrafficLight(GC.USA_INTERSECTION_ID, GC.TL_NORTHNORTH_THROUGHLANE, GC.RED)
    TrafficLightObjectList[5] = TL.TrafficLight(GC.USA_INTERSECTION_ID, GC.TL_NORTHWEST_TURNINGLANE, GC.RED)
    TrafficLightObjectList[6] = TL.TrafficLight(GC.USA_INTERSECTION_ID, GC.TL_EASTEAST_THROUGHLANE, GC.GREEN)
    TrafficLightObjectList[7] = TL.TrafficLight(GC.USA_INTERSECTION_ID, GC.TL_EASTNORTH_TURNINGLANE, GC.RED)

    controlSystem = Intersection.Intersection()
    Machine(model=controlSystem, states=possibleStates, transitions=trafficFlowTransitions, initial='ALL_RED')

    # Default to East/West through as the first State Machine state
    controlSystem.start()
    DebugObject.Dprint(controlSystem.state)
    prevState = 'ALL_RED'

    loopTime = 0
    DebugObject.Dprint("STARTING LOOP")
    while(True):
        loopTime = (loopTime + TIME_STEP)

        sensors = GetActiveVehicleSensors()
        DebugObject.Dprint(loopTime)
        DebugObject.Dprint("SENSOR STATE = " + str(sensors))
        prevState = controlSystem.state

        if((not sensors[GC.TL_SOUTHEAST_TURNINGLANE] and not sensors[GC.TL_NORTHWEST_TURNINGLANE] and loopTime > GC.NS_TURNING_MIN) or loopTime > GC.NS_TURNING_MAX):  # NOQA: E501
            if(sensors[GC.TL_NORTHNORTH_THROUGHLANE] or sensors[GC.TL_SOUTHSOUTH_THROUGHLANE]):
                if(controlSystem.state == 'NS_TURNING'):
                    loopTime = 0
                    controlSystem.NS_THROUGH_ONLY()

        if((not sensors[GC.TL_SOUTHSOUTH_THROUGHLANE] and not sensors[GC.TL_NORTHNORTH_THROUGHLANE] and loopTime > GC.NS_THROUGH_MIN) or loopTime > GC.NS_THROUGH_MAX):  # NOQA: E501
            if(sensors[GC.TL_SOUTHEAST_TURNINGLANE] or sensors[GC.TL_NORTHWEST_TURNINGLANE]):
                if(controlSystem.state == 'NS_THROUGH'):
                    loopTime = 0
                    controlSystem.ALLOW_EW_TURNING()

        if((not sensors[GC.TL_WESTSOUTH_TURNINGLANE] and not sensors[GC.TL_EASTNORTH_TURNINGLANE] and loopTime > GC.EW_TURNING_MIN) or loopTime > GC.EW_TURNING_MAX):  # NOQA: E501
            if(sensors[GC.TL_WESTWEST_THROUGHLANE] or sensors[GC.TL_EASTEAST_THROUGHLANE]):
                if(controlSystem.state == 'EW_TURNING'):
                    loopTime = 0
                    controlSystem.EW_THROUGH_ONLY()

        if((not sensors[GC.TL_WESTWEST_THROUGHLANE] and not sensors[GC.TL_EASTEAST_THROUGHLANE] and loopTime > GC.EW_THROUGH_MIN) or loopTime > GC.EW_THROUGH_MAX):  # NOQA: E501
            if(sensors[GC.TL_EASTNORTH_TURNINGLANE] or sensors[GC.TL_WESTSOUTH_TURNINGLANE]):
                if(controlSystem.state == 'EW_THROUGH'):
                    loopTime = 0
                    controlSystem.ALLOW_NS_TURNING()

        UpdateTrafficLights(TrafficLightObjectList, controlSystem, prevState)


if __name__ == "__main__":
    if(UNIT_TEST_MODE):
        UnitTest(2)
    else:
        Main()
