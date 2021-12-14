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

import PySimpleGUI as sg

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


<<<<<<< Updated upstream
if __name__ == "__main__":
    # Allow URLs to be refreshed (F5) without restarting web server after code changes
    app.run(debug=True)
    app.run(host='0.0.0.0')

    ItemsToUpdate = [0, 1, 1, 1, 1, 0, 0, 0]
    ObjectList = [0, 1, 1, 1, 1, 0, 0, 0]
    GUI_Update(ItemsToUpdate, ObjectList)
=======
    app = QtWidgets.QApplication(sys.argv)
    #https://doc.qt.io/qtforpython/PySide6/QtGui/index.html#module-PySide6.QtGui
    #https://stackoverflow.com/questions/52517516/pyqt5-fixed-window-size
    label = QLabel("Hello World", alignment=Qt.AlignCenter)
    label.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":

    sg.theme('DarkAmber')   # Add a touch of color

    # All the stuff inside your window.
    layout = [[sg.Text('Some text on Row 1')], [sg.Text('Enter something on Row 2'), sg.InputText()], [sg.Button('Ok'), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Loft Orbital Traffic Light Demo', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        print('You entered ', values[0])

    window.close()
>>>>>>> Stashed changes
