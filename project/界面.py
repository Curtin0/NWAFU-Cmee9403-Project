
from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(225, 250)
        
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 170, 40))
        self.pushButton.setStyleSheet("font: 12pt \"黑体\";")
        self.pushButton.setObjectName("pushButton")
        
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(50, 100, 300, 80))
        self.label.setStyleSheet("font: 16pt \"黑体\";")
        self.label.setObjectName("label")
        
        self.label_0 = QtWidgets.QLabel(MainWindow)
        self.label_0.setGeometry(QtCore.QRect(50, 160, 120, 50))
        self.label_0.setStyleSheet("background-color: rgb(255, 255, 255); font: 12pt \"黑体\";")
        self.label_0.setObjectName("textEdit")
        
        self.retranslateUi(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "结果显示："))
        self.pushButton.setText(_translate("MainWindow", "传感器输入高电平"))

