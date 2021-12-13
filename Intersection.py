#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__company__ = "Loft Orbitial"
__status__  = "Development"
__date__    = "Late Updated: 2021-12-12"
__doc__     = "Skeleton class to initialize 'from transitions import Machine, State' with"
"""

# Useful global constants used across all classes
import GlobalConstant as GC

# Allows for the creation of a GUI web app that communicates with python backend code
# Saves HTML files in a folder called "templates" in the same folder as your Flask code
# Saves user state / data across page refreshes and crashes, by using browser cookies
from flask import Flask, render_template

# Click on HTML table to update GUI / CSS classes
import pyautogui


class Intersection(object):
    pass


controlSystem = Intersection()

# Make a Flask application and start running code from Main()
app = Flask(__name__)


@app.route('/')
def GUI_Update(ItemsToUpdate, ObjectList):
    HTMLtoDisplay = "TrafficSignals.html"

    if(ItemsToUpdate == GC.TRAFFIC_LIGHT_GUI):
        return render_template(HTMLtoDisplay, lightValue=ObjectList)
    elif(ItemsToUpdate == GC.TRAFFIC_LIGHT_GUI):
        return render_template(HTMLtoDisplay, sensorValue=ObjectList)
    else:
        print("ERROR UPDATING GUI")

    pyautogui.moveTo(900, 500)
    pyautogui.click()


if __name__ == "__main__":
    # Allow URLs to be refreshed (F5) without restarting web server after code changes
    app.run(debug=True)
    app.run(host='0.0.0.0')

    ItemsToUpdate = [0, 1, 1, 1, 1, 0, 0, 0]
    ObjectList = [0, 1, 1, 1, 1, 0, 0, 0]
    GUI_Update(ItemsToUpdate, ObjectList)
