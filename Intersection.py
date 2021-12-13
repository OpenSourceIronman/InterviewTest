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

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication,  QMainWindow, QLabel


class Intersection(object):
    pass


controlSystem = Intersection()

newSensorsGUI = [0, 1, 1, 1, 1, 0, 0, 0]
newTrafficLightGUI = [0, 1, 1, 1, 1, 0, 0, 0]


def stuff():
    app = gui("Loft Orbital Traffic Light Demo", "1000x1000")
    app.addLabel("title", "Welcome to appJar")
    app.setLabelBg("title", "red")
    app.go()
    
    app.addLabel("blank0", "", 0, 0)
    app.setLabelBg("blank0", "white")
    app.addLabel("blank1", "", 0, 1)
    app.addLabel("blank2", "", 0, 2)
    app.addLabel("road0", "S:S", 0, 3)
    app.addLabel("road1", "S:E", 0, 4)
    app.addLabel("road2", "", 0, 5)
    app.addLabel("road3", "", 0, 6)
    app.addLabel("blank3", "", 0, 7)
    app.addLabel("blank4", "", 0, 8)
    app.addLabel("blank5", "", 0, 9)
    app.setFg("white")
    app.setLocation("CENTER")
    app.setFont(18)
    #app.setSticky("news")
    #app.setExpand("both")

    #app.addImage("sign0", "Straight_100x100_180.png", )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyPyForm = QMainWindow()
    MyPyForm.setGeometry(1500, 1000, 3300, 2500)
    
    label = QLabel("Hello World", alignment=Qt.AlignCenter)
    label.show()
    sys.exit(app.exec_())
