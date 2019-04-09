#from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
#now = QDate.currentDate()
##print(now)
#print(now.toString(Qt.ISODate))
#print(now.toString(Qt.DefaultLocaleLongDate))
#print('')
#
#dateTime = QDateTime.currentDateTime()
#print(dateTime.toString())
#print("Print the Month:")
#getTimeStr = dateTime.toString()
#
#print(getTimeStr[4:7])
#time = QTime.currentTime()
#print(time.toString(Qt.DefaultLocaleLongDate))
#
#
#d = QDate(1945,5,7)
#print("Days in Month: %s" % d.daysInMonth())
#print("Days in year: %s" % d.daysInYear())
#
#xmas1 = QDate(2019,12,24)
#xmas2 = QDate(2018,12,24)
#
#now = QDate.currentDate()
#daysPassed = xmas2.daysTo(now)
#print("%s days passed since last Christmas: " % daysPassed)
#
## Datetime arithmetic 
#
#now = QDateTime.currentDateTime()
#print("Today: %s" % now.toString(Qt.ISODate))
#print("Adding 12 days: %s" % now.addDays(12).toString(Qt.ISODate))
#print("Subtracting 22 days: %s" % now.addDays(-22).toString(Qt.ISODate))
#print("Adding 55 seconds: %s" % now.addSecs(55).toString(Qt.ISODate))
#print("Adding 3 Months: %s" % now.addMonths(3).toString(Qt.ISODate))
#print("Adding 12 years: %s" % now.addYears(12).toString(Qt.ISODate))
#
## Daylight saving time (DST)
#from PyQt5.QtCore import QTimeZone
#now = QDateTime.currentDateTime()
#print("Time Zone: %s" % now.timeZoneAbbreviation())
#
#if now.isDaylightTime():
#    print("The current date falls into DST Time")
#else:
#    print("The current date does not fall into DST Time")
#    
## A simple window 
#import sys 
#from PyQt5.QtWidgets import QApplication, QWidget
#from PyQt5.QtGui import QIcon
#
##app = QApplication(sys.argv)
##w = QWidget()
##w.resize(350, 150)
##w.move(300, 300)
##w.setWindowTitle("Simple")
##w.show()
##
##sys.exit(app.exec_())
#
#class Example(QWidget):
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#    def initUI(self):
#        self.setGeometry(300,300,300,227)
#        self.setWindowTitle("Icon")
#        self.setWindowIcon(QIcon("output-onlinepngtools.png"))
#        self.show()
#        
#app = QApplication(sys.argv)
#ex = Example()
##sys.exit
#
## push button 
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox)
#import sys 
#from PyQt5.QtGui import QFont
#
#class Example(QWidget):
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#    def initUI(self):
#        QToolTip.setFont(QFont('SansSerif', 10))
#        self.setToolTip("This is a <b>QWidget</b> widget")
#        btn = QPushButton("Button", self)
#        btn.setToolTip("This is a <b>QPushButton </b> widget")
#        btn.resize(btn.sizeHint())
#        btn.move(50,50)
#        self.setGeometry(300,300,300,200)
#        self.setWindowTitle('Tool Tips')
#        self.show()
#        def closeEvent(self,event):
#            reply = QMessageBox.question(self,'Message', "Are you sure you want to quit?", 
#                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#            if reply == QMessageBox.Yes:
#                event.accept()
#            else:
#                event.ignore()
#app = QApplication(sys.argv)
#ex = Example()
##sys.exit()

# Centering a window on a screen
from PyQt5.QtWidgets import QDesktopWidget
import sys
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(450, 450)
        self.center()
        self.setWindowTitle('Center')
        self.show()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
app = QApplication(sys.argv)
ex = Example() 
app.exec_()
