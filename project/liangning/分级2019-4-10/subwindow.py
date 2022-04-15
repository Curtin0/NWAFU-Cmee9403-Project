from PyQt5 import QtCore, QtWidgets, QtGui

class Ui_SubWindow(object):
    def setupUi(self, SubWindow):

        SubWindow.setObjectName("SubWindow")
        SubWindow.setGeometry(QtCore.QRect(500, 300, 300, 200))
        
        self.comboBox = QtWidgets.QComboBox(SubWindow)
        self.comboBox.setGeometry(QtCore.QRect(90, 25, 120, 50))
        self.comboBox.setStyleSheet("font: 75 14pt \"楷体\";")
        self.comboBox.addItem("一档速度")
        self.comboBox.addItem("二档速度")
        self.comboBox.addItem("三档速度")
        self.comboBox.setCurrentIndex(0)
        self.comboBox.setObjectName("comboBox")
        
        self.button_returning = QtWidgets.QPushButton(SubWindow)
        self.button_returning.setGeometry(QtCore.QRect(110, 122, 80, 40))
        self.button_returning.setStyleSheet("font: 14pt \"宋体\";")
        
        self.retranslateUi(SubWindow)
        
    def retranslateUi(self, SubWindow):
        _translate = QtCore.QCoreApplication.translate
        SubWindow.setWindowTitle(_translate("SubWindow", "工作速度档位选择"))
        self.button_returning.setText(_translate("SubWindow", "开始运行"))