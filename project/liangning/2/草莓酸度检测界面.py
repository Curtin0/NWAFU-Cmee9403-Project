import sys
from 草莓酸度检测 import Ui_MainWindow
from PyQt5 import QtWidgets


class mywindow(QtWidgets.QWidget,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pHcalc)

    def pHcalc(self):
        text= self.comboBox.currentText()
        if text == "新星2号":
            DL = int(self.dl_value.value())
            pH = ((DL - 53.388) / 11.029)
            total_pH_string = "The pH is: " + str(pH)
            self.label_5.setText(total_pH_string)
        
        elif text == "全明星":
            DL = int(self.dl_value.value())
            pH = ((DL - 118.78) / 12.568)
            total_pH_string = "The pH is: " + str(pH)
            self.label_5.setText(total_pH_string)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())