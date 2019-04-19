# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:28:49 2019

@author: Zane
"""

#import serial 
#import matplotlib.pyplot as plt
#
#ser = serial.Serial('COM3', 9600)
#n = 0
#dataLst = []
#while n < 200: 
#    print(ser.readline())
#    dataPoint = ser.readline()
#    dataPoint = int(dataPoint)
#    dataLst.append(dataPoint)
#    n += 1
#    
#ser.close()
#
#plt.plot(dataLst)
#plt.show()
#f = open("serialData.dat", "w")
#f.write(str(dataLst))
#f.close()
#f = open('serialData.dat', 'r')
#print(f.read())

# Task 2
#import pyqtgraph as pg
#from pyqtgraph.Qt import QtCore, QtGui
#from pyqtgraph import PlotWidget
#import numpy as np
#
#x = np.array([1,2,3])
#y = np.array([1,2,3])
#pg.setConfigOption('background', 'w')
#penn = pg.mkPen('k', width = 2, style = QtCore.Qt.SolidLine)
#pl = pg.plot(x,y, pen = penn, title = 'The first pyqtgraph plot', sysmbol = 't', symbolSize = 20)
#pl.setXRange(0,4)
#pl.setYRange(0,4)
#pl.setLabel('left', 'Voltage', 'V')
#pl.setLabel('bottom', 'Time', 's')
#
#QtGui.QApplication.exec_()


# Task 2 pt 2

#from PyQt5 import QtGui, QtCore
#import pyqtgraph as pg 
## Always start by initializing Qt (only once per application)
#app = QtGui.QApplication([])
## define a top-level widget to hold everything
#w = QtGui.QWidget()
## Create some widgets to be placed inside 
#btn = QtGui.QPushButton('Press Me!')
#text = QtGui.QLineEdit('enter text')
#listw = QtGui.QListWidget()
#pg.setConfigOption('background', 'w')
#plt = pg.PlotWidget() # pg.PlotWidget allows the use of the properties below but pg.plot does not
#penn = pg.mkPen('k', width = 2, style = QtCore.Qt.SolidLine)
#plt.plot([1,2,3], [1,2,3], pen = penn, title = 'The first pyqtgraph plot', symbol = 't',
#         symbolSize = 20)
#labelStyle = {'color': '#000', 'font-size':'30px'}
#plt.setLabel('bottom', 'Time', 's', **labelStyle)
#plt.setLabel('left', 'Voltage', 'V', **labelStyle)
#plt.setYRange(0,5)
#plt.setXRange(0,5)
### Create a grid layout to manage the widgets size and position
#layout = QtGui.QGridLayout()
#w.setLayout(layout)
## Add widgets to the layout in the proper positions
#layout.addWidget(btn, 0, 0) # button goes in upper-left
#layout.addWidget(text, 1, 0) # Text edit goes in middle left
#layout.addWidget(listw, 2, 0) # list widget goe sin bottom-left
#layout.addWidget(plt, 0, 1, 3, 1) # plot goes on right side, spannig 3 rows
## and 1 column
## Display the widget as a new window 
#w.show()
## start the Qt event loop 
#app.exec_()

# task 3 live plot the serial data with the pywtgraph 
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import serial 
from PyQt5 import QtGui, QtCore
import sys 
import numpy as np 
import pyqtgraph

ser = serial.Serial('COM3', 9600)

class ExampleApp(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        pyqtgraph.setConfigOption('background', 'w')
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        # plot widget
        self.graphicsView = PlotWidget(self.centralwidget) # assign this plotwidget to the graphicsView
        self.graphicsView.setObjectName("graphicsView")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
    def update(self):
        points = 100
        x = np.array(points)
        n = 0
        dataLst = []
        while n < 200:
            dataPoint = ser.readline()
            dataPoint = int(dataPoint)
            dataLst.append(dataPoint)
            n += 1
        y = dataLst
        penn = pyqtgraph.mkPen('k', width = 3, style = QtCore.Qt.SolidLine)
        self.graphicsView.setYRange(0, 1200, padding = 0)
        labelStyle = {'color': '#000', 'font-size' : '20px'}
        self.graphicsView.setLabel('bottom', 'Number of Points', '', **labelStyle)
        self.graphicsView.plot(x,y, pen = penn, clear = True)
        QtCore.QTimer.singleShot(1,self.update)
        

app = QtGui.QApplication(sys.argv)
form = ExampleApp()
form.show()
form.update()
app.exec_()
