#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__company__ = "Loft Orbitial"
__status__  = "Development"
__date__    = "Late Updated: 2021-12-14"
__doc__     = "Intersection GUI and State Machine high level object"
"""

# Useful global constants used across all classes
import GlobalConstant as GC

# A cross-platform GUI toolkit
# https://www.wxpython.org/
import wx
import wx.grid


class Intersection(object):
    pass


controlSystem = Intersection()


class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title='Loft Orbital Traffic Light Demo', size=(1000, 1000))

        # Create background panel inide Window
        panel = wx.Panel(self, size=(1000, 1000))
        panel.SetBackgroundColour(wx.BLACK)

        # Create 10 x 10 grid with each cell being of size 100 x 100 pixels
        # https://wxpython.org/Phoenix/docs/html/grid_overview.html
        self.grid = wx.grid.Grid(self, -1, size=(1000, 1000), style=wx.ALIGN_CENTER_VERTICAL)
        self.grid.CreateGrid(10, 10)
        for i in range(10):
            self.grid.SetRowSize(i, 100)
            self.grid.SetColSize(i, 100)
        self.grid.HideColLabels()
        self.grid.HideRowLabels()

        # Change color of cells not part of intersection to white
        for row in range(3):
            for col in range(3):
                self.grid.SetCellBackgroundColour(row, col, wx.WHITE)
            for col in range(7, 10):
                self.grid.SetCellBackgroundColour(row, col, wx.WHITE)

        for row in range(7, 10):
            for col in range(3):
                self.grid.SetCellBackgroundColour(row, col, wx.WHITE)
            for col in range(7, 10):
                self.grid.SetCellBackgroundColour(row, col, wx.WHITE)

        self.Show()

    def GUI_Update(self, grid, sensorList, trafficLightList):
        """Update the color of grid cells in a WxPython Window

        Args:
            grid (wx.grid): A WxPython Grid object that holds cell attritubes such as color
            sensorList (List)): New TRUE/FALSE states of road sensors to display in GUI
            trafficLightList (List): New TrafficLight objects to display in GUI
        """

        # Update color changes all in ONE for loop to keep at O(n) and not O(n^2)
        for i in range(GC.LANE_COUNT):
            if(sensorList[i]):
                sensorColor = wx.YELLOW  # Car above road sensor
            else:
                sensorColor = wx.BLACK

            if(trafficLightList[i]):
                lightColor = wx.GREEN
            else:
                lightColor = wx.RED

            # Map index of both the trafficLightList and sensorList to a hard coded grid locations
            if(i == GC.TL_SOUTHSOUTH_THROUGHLANE):
                self.grid.SetCellBackgroundColour(2, 3, sensorColor)
                self.grid.SetCellBackgroundColour(7, 3, lightColor)
            if(i == GC.TL_SOUTHEAST_TURNINGLANE):
                self.grid.SetCellBackgroundColour(2, 4, sensorColor)
                self.grid.SetCellBackgroundColour(7, 4, lightColor)

            if(i == GC.TL_WESTWEST_THROUGHLANE):
                self.grid.SetCellBackgroundColour(3, 7, sensorColor)
                self.grid.SetCellBackgroundColour(3, 2, lightColor)
            if(i == GC.TL_WESTSOUTH_TURNINGLANE):
                self.grid.SetCellBackgroundColour(4, 7, sensorColor)
                self.grid.SetCellBackgroundColour(4, 2, lightColor)

            if(i == GC.TL_NORTHNORTH_THROUGHLANE):
                self.grid.SetCellBackgroundColour(7, 6, sensorColor)
                self.grid.SetCellBackgroundColour(2, 6, lightColor)
            if(i == GC.TL_NORTHWEST_TURNINGLANE):
                self.grid.SetCellBackgroundColour(7, 5, sensorColor)
                self.grid.SetCellBackgroundColour(2, 5, lightColor)
            if(i == GC.TL_EASTEAST_THROUGHLANE):
                self.grid.SetCellBackgroundColour(6, 2, sensorColor)
                self.grid.SetCellBackgroundColour(6, 7, lightColor)
            if(i == GC.TL_EASTNORTH_TURNINGLANE):
                self.grid.SetCellBackgroundColour(5, 2, sensorColor)
                self.grid.SetCellBackgroundColour(5, 7, lightColor)


if __name__ == "__main__":

    app = wx.App()
    frame = MyFrame()

    sensorList = [0, 0, 0, 1, 1, 1, 0, 1]
    trafficLightList = [0, 1, 0, 0, 0, 1, 0, 0]

    frame.GUI_Update(frame.grid, sensorList, trafficLightList)
    app.MainLoop()
