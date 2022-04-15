import RPi.GPIO as GPIO 
import time
import sys

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO_OUT = 11 
GPIO.setup(GPIO_OUT,GPIO.IN)

Relay_Ch1 = 12 
Relay_Ch2 = 13 
Relay_Ch3 = 15 
Relay_Ch4 = 16 

GPIO.setup(Relay_Ch1,GPIO.OUT)
GPIO.setup(Relay_Ch2,GPIO.OUT)
GPIO.setup(Relay_Ch3,GPIO.OUT)
GPIO.setup(Relay_Ch4,GPIO.OUT)

from 界面 import Ui_MainWindow
from PyQt5 import QtWidgets

class mywindow(QtWidgets.QWidget,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.i = 0

        self.pushButton.clicked.connect(self.click)
        
    def click(self):
        text=["12","13","15","16"]
        if GPIO.IN == GPIO.HIGH:
            if text[self.i] == "12":
                self.lab_0.setText("1号阀门打开")
                GPIO.output(Relay_Ch1,GPIO.HIGH) 
                time.sleep(0.5)
                GPIO.output(Relay_Ch1,GPIO.LOW)
            elif text[self.i] =="13":
                self.lab_0.setText("2号阀门打开")
                GPIO.output(Relay_Ch2,GPIO.HIGH) 
                time.sleep(0.5)
                GPIO.output(Relay_Ch2,GPIO.LOW)
            elif text[self.i] =="15":
                self.lab_0.setText("3号阀门打开")
                GPIO.output(Relay_Ch3,GPIO.HIGH) 
                time.sleep(0.5)
                GPIO.output(Relay_Ch3,GPIO.LOW)
            else:
                self.lab_0.setText("4号阀门打开")
                GPIO.output(Relay_Ch4,GPIO.HIGH) 
                time.sleep(0.5)
                GPIO.output(Relay_Ch4,GPIO.LOW)
            self.i += 1
            if self.i == 4:
                self.i = 0

        else:
            click() 
            
              
GPIO.cleanup()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
