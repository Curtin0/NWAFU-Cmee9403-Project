from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(120, 80, 561, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)

        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 24pt \"楷体\";")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(130, 170, 261, 81))
        self.label_2.setStyleSheet("font: 75 20pt \"楷体\";")
        self.label_2.setObjectName("label_2")

        self.dl_value = QtWidgets.QSpinBox(MainWindow)
        self.dl_value.setGeometry(QtCore.QRect(420, 190, 261, 40))
        self.dl_value.setStyleSheet("font: 75 20pt \"Times New Roman\";")
        self.dl_value.setMaximum(1000)
        self.dl_value.setSingleStep(10)
        self.dl_value.setProperty("value", 100)
        self.dl_value.setObjectName("dl_value")

        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(130, 260, 261, 81))
        self.label_3.setStyleSheet("font: 75 20pt \"楷体\";")
        self.label_3.setObjectName("label_3")

        self.comboBox = QtWidgets.QComboBox(MainWindow)
        self.comboBox.setGeometry(QtCore.QRect(280, 280, 201, 40))
        self.comboBox.setStyleSheet("font: 75 20pt \"楷体\";")
        self.comboBox.setMaxCount(5)
        self.comboBox.addItem("新星2号")
        self.comboBox.addItem("全明星")
        self.comboBox.setCurrentIndex(0)
        self.comboBox.setObjectName("comboBox")

        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(130, 360, 261, 81))
        self.label_4.setStyleSheet("font: 75 20pt \"楷体\";")
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(359, 380, 321, 50))
        self.label_5.setStyleSheet("font: 75 20pt \"楷体\";")
        self.label_5.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(500, 280, 181, 40))
        self.pushButton.setStyleSheet("font: 75 20pt \"楷体\";")
        self.pushButton.setObjectName("pushButton")

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "基于微弱光的草莓酸度检测系统"))
        self.label_2.setText(_translate("MainWindow", "延迟发光光子数："))
        self.label_3.setText(_translate("MainWindow", "品种选择："))
        self.label_4.setText(_translate("MainWindow", "计算结果显示："))
        self.pushButton.setText(_translate("MainWindow", "pH值计算"))

