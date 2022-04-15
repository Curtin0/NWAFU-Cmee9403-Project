# import os
import sys
# import cv2
import numpy as np
# import RPi.GPIO as GPIO
from yancaochuli import Ui_MWindow
from PyQt5 import QtWidgets, QtGui, QtCore

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 新建窗体，建标签、按钮
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font_bold = QtGui.QFont()
        font_bold.setFamily("宋体")
        font_bold.setPointSize(14)
        font_bold.setBold(True)
        font_bold.setWeight(75)
        
        self.groupBox_imageRegion = QtWidgets.QGroupBox(MainWindow)
        self.groupBox_imageRegion.setGeometry(QtCore.QRect(15, 15, 1050, 365))
        self.groupBox_imageRegion.setFont(font_bold)
        
        self.label_imageRegion = QtWidgets.QLabel(MainWindow)
        self.label_imageRegion.setGeometry(QtCore.QRect(15, 15, 120, 40))
        
        self.label_cameraImage_front  = QtWidgets.QLabel(MainWindow)
        self.label_cameraImage_front.setGeometry(QtCore.QRect(35, 55, 200, 150))
        self.label_cameraImage_front.setStyleSheet("background-color: rgb(127, 127, 127);")
        
        self.label_originalImage_front = QtWidgets.QLabel(MainWindow)
        self.label_originalImage_front.setGeometry(QtCore.QRect(237, 55, 200, 150))
        self.label_originalImage_front.setStyleSheet("background-color: rgb(127, 127, 127);")

        self.label_diseaseImage_front = QtWidgets.QLabel(MainWindow)
        self.label_diseaseImage_front.setGeometry(QtCore.QRect(439, 55, 200, 150))
        self.label_diseaseImage_front.setStyleSheet("background-color: rgb(127, 127, 127);")

        self.label_crackleImage_front = QtWidgets.QLabel(MainWindow)
        self.label_crackleImage_front.setGeometry(QtCore.QRect(641, 55, 200, 150))
        self.label_crackleImage_front.setStyleSheet("background-color: rgb(127, 127, 127);")

        self.label_gradeImage_front = QtWidgets.QLabel(MainWindow)
        self.label_gradeImage_front.setGeometry(QtCore.QRect(843, 55, 200, 150))
        self.label_gradeImage_front.setStyleSheet("background-color: rgb(127, 127, 127);")

        self.label_cameraImage_back  = QtWidgets.QLabel(MainWindow)
        self.label_cameraImage_back.setGeometry(QtCore.QRect(35, 215, 200, 150))
        self.label_cameraImage_back.setStyleSheet("background-color: rgb(127, 127, 127);")
        
        self.label_originalImage_back = QtWidgets.QLabel(MainWindow)
        self.label_originalImage_back.setGeometry(QtCore.QRect(237, 215, 200, 150))
        self.label_originalImage_back.setStyleSheet("background-color: rgb(127, 127, 127);")

        self.label_diseaseImage_back = QtWidgets.QLabel(MainWindow)
        self.label_diseaseImage_back.setGeometry(QtCore.QRect(439, 215, 200, 150))
        self.label_diseaseImage_back.setStyleSheet("background-color: rgb(127, 127, 127);")

        self.label_crackleImage_back = QtWidgets.QLabel(MainWindow)
        self.label_crackleImage_back.setGeometry(QtCore.QRect(641, 215, 200, 150))
        self.label_crackleImage_back.setStyleSheet("background-color: rgb(127, 127, 127);")

        self.label_gradeImage_back = QtWidgets.QLabel(MainWindow)
        self.label_gradeImage_back.setGeometry(QtCore.QRect(843, 215, 200, 150))
        self.label_gradeImage_back.setStyleSheet("background-color: rgb(127, 127, 127);")

        self.groupBox_controlRegion = QtWidgets.QGroupBox(MainWindow)
        self.groupBox_controlRegion.setGeometry(QtCore.QRect(15, 400, 1050, 90))
        self.groupBox_controlRegion.setFont(font_bold)
        
        self.button_workingSpeed = QtWidgets.QPushButton(MainWindow)
        self.button_workingSpeed.setGeometry(QtCore.QRect(110, 438, 100, 40))
        self.button_workingSpeed.setStyleSheet("font: 12pt \"宋体\";")
        
        self.button_openCamera = QtWidgets.QPushButton(MainWindow)
        self.button_openCamera.setGeometry(QtCore.QRect(360, 438, 100, 40))
        self.button_openCamera.setStyleSheet("font: 12pt \"宋体\";")

        self.button_signalTrigger = QtWidgets.QPushButton(MainWindow)
        self.button_signalTrigger.setGeometry(QtCore.QRect(610, 438, 100, 40))
        self.button_signalTrigger.setStyleSheet("font: 12pt \"宋体\";")

        self.button_initialWindow = QtWidgets.QPushButton(MainWindow)
        self.button_initialWindow.setGeometry(QtCore.QRect(870, 438, 100, 40))
        self.button_initialWindow.setStyleSheet("font: 12pt \"宋体\";")
        
        self.groupBox_resultRegion = QtWidgets.QGroupBox(MainWindow)
        self.groupBox_resultRegion.setGeometry(QtCore.QRect(15, 510, 1050, 180))
        self.groupBox_resultRegion.setFont(font_bold)
        
        self.label_quantity = QtWidgets.QLabel(MainWindow)
        self.label_quantity.setGeometry(QtCore.QRect(30, 605, 50, 25))
        self.label_quantity.setStyleSheet("font: 14pt \"宋体\";")
        
        self.label_proportion = QtWidgets.QLabel(MainWindow)
        self.label_proportion.setGeometry(QtCore.QRect(30, 640, 50, 25))
        self.label_proportion.setStyleSheet("font: 14pt \"宋体\";")

        font_noBold = QtGui.QFont()
        font_noBold.setFamily("宋体")
        font_noBold.setPointSize(14)
        
        self.groupBox_disease = QtWidgets.QGroupBox(MainWindow)
        self.groupBox_disease.setGeometry(QtCore.QRect(80, 540, 235, 140))
        self.groupBox_disease.setFont(font_noBold)
        
        self.label_yesDisease = QtWidgets.QLabel(MainWindow)
        self.label_yesDisease.setGeometry(QtCore.QRect(120, 575, 60, 25))

        self.label_noDisease = QtWidgets.QLabel(MainWindow)
        self.label_noDisease.setGeometry(QtCore.QRect(220, 575, 60, 25))
        
        self.label_yesDisease_Quantity = QtWidgets.QLabel(MainWindow)
        self.label_yesDisease_Quantity.setGeometry(QtCore.QRect(120, 605, 55, 25))
        self.label_yesDisease_Quantity.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.label_yesDisease_Proportion = QtWidgets.QLabel(MainWindow)
        self.label_yesDisease_Proportion.setGeometry(QtCore.QRect(120, 640, 55, 25))
        self.label_yesDisease_Proportion.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.label_noDisease_Quantity = QtWidgets.QLabel(MainWindow)
        self.label_noDisease_Quantity.setGeometry(QtCore.QRect(220, 605, 55, 25))
        self.label_noDisease_Quantity.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.label_noDisease_Proportion = QtWidgets.QLabel(MainWindow)
        self.label_noDisease_Proportion.setGeometry(QtCore.QRect(220, 640, 55, 25))
        self.label_noDisease_Proportion.setStyleSheet("background-color: rgb(255, 255, 255);")
 
        self.groupBox_crackle = QtWidgets.QGroupBox(MainWindow)
        self.groupBox_crackle.setGeometry(QtCore.QRect(330, 540, 235, 140))
        self.groupBox_crackle.setFont(font_noBold)

        self.label_yesCrackle = QtWidgets.QLabel(MainWindow)
        self.label_yesCrackle.setGeometry(QtCore.QRect(370, 575, 60, 25))
 
        self.label_noCrackle = QtWidgets.QLabel(MainWindow)
        self.label_noCrackle.setGeometry(QtCore.QRect(470, 575, 60, 25))
        
        self.label_yesCrackle_Quantity = QtWidgets.QLabel(MainWindow)
        self.label_yesCrackle_Quantity.setGeometry(QtCore.QRect(370, 605, 55, 25))
        self.label_yesCrackle_Quantity.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.label_yesCrackle_Proportion = QtWidgets.QLabel(MainWindow)
        self.label_yesCrackle_Proportion.setGeometry(QtCore.QRect(370, 640, 55, 25))
        self.label_yesCrackle_Proportion.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.label_noCrackle_Quantity = QtWidgets.QLabel(MainWindow)
        self.label_noCrackle_Quantity.setGeometry(QtCore.QRect(470, 605, 55, 25))
        self.label_noCrackle_Quantity.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.label_noCrackle_Proportion = QtWidgets.QLabel(MainWindow)
        self.label_noCrackle_Proportion.setGeometry(QtCore.QRect(470, 640, 55, 25))
        self.label_noCrackle_Proportion.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.groupBox_grade = QtWidgets.QGroupBox(MainWindow)
        self.groupBox_grade.setGeometry(QtCore.QRect(580, 540, 470, 140))
        self.groupBox_grade.setFont(font_noBold)
        
        self.label_specialGrade  = QtWidgets.QLabel(MainWindow)
        self.label_specialGrade.setGeometry(QtCore.QRect(621, 575, 60, 25))
 
        self.label_firstGrade = QtWidgets.QLabel(MainWindow)
        self.label_firstGrade.setGeometry(QtCore.QRect(732, 575, 60, 25))
        
        self.label_secondGrade = QtWidgets.QLabel(MainWindow)
        self.label_secondGrade.setGeometry(QtCore.QRect(844, 575, 60, 25))
        
        self.label_thirdGrade = QtWidgets.QLabel(MainWindow)
        self.label_thirdGrade.setGeometry(QtCore.QRect(955, 575, 60, 25))
        
        self.label_specialGrade_Quantity = QtWidgets.QLabel(MainWindow)
        self.label_specialGrade_Quantity.setGeometry(QtCore.QRect(621, 605, 55, 25))
        self.label_specialGrade_Quantity.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.label_specialGrade_Proportion = QtWidgets.QLabel(MainWindow)
        self.label_specialGrade_Proportion.setGeometry(QtCore.QRect(621, 640, 55, 25))
        self.label_specialGrade_Proportion.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.label_firstGrade_Quantity = QtWidgets.QLabel(MainWindow)
        self.label_firstGrade_Quantity.setGeometry(QtCore.QRect(732, 605, 55, 25))
        self.label_firstGrade_Quantity.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.label_firstGrade_Proportion = QtWidgets.QLabel(MainWindow)
        self.label_firstGrade_Proportion.setGeometry(QtCore.QRect(732, 640, 55, 25))
        self.label_firstGrade_Proportion.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.label_secondGrade_Quantity = QtWidgets.QLabel(MainWindow)
        self.label_secondGrade_Quantity.setGeometry(QtCore.QRect(844, 605, 55, 25))
        self.label_secondGrade_Quantity.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.label_secondGrade_Proportion = QtWidgets.QLabel(MainWindow)
        self.label_secondGrade_Proportion.setGeometry(QtCore.QRect(844, 640, 55, 25))
        self.label_secondGrade_Proportion.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.label_thirdGrade_Quantity = QtWidgets.QLabel(MainWindow)
        self.label_thirdGrade_Quantity.setGeometry(QtCore.QRect(955, 605, 55, 25))
        self.label_thirdGrade_Quantity.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.label_thirdGrade_Proportion = QtWidgets.QLabel(MainWindow)
        self.label_thirdGrade_Proportion.setGeometry(QtCore.QRect(955, 640, 55, 25))
        self.label_thirdGrade_Proportion.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        # 设置窗口和显示标签名字
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.timer_showCamera = QtCore.QTimer()
        # self.cap_front = cv2.VideoCapture()
        # self.cap_back = cv2.VideoCapture()
        self.num_write = 0
        self.num_read = 0
        self.value_judgement = 0
        self.yesDisease_front = 0
        self.yesDisease_back = 0
        self.yesCrackle_front = 0
        self.yesCrackle_back = 0
        self.SUM_yesDisease = 0
        self.SUM_noDisease = 0
        self.SUM_yesCrackle = 0
        self.SUM_noCrackle = 0
        self.SUM_specialGrade = 0
        self.SUM_firstGrade = 0
        self.SUM_secondGrade = 0
        self.SUM_thirdGrade = 0

        self.button_workingSpeed.clicked.connect(self.workingSpeed)
        self.button_openCamera.clicked.connect(self.openCamera)
        self.timer_showCamera.timeout.connect(self.showCamera)
        self.button_signalTrigger.clicked.connect(self.signalTrigger)
        self.button_initialWindow.clicked.connect(self.initialWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于机器视觉的红枣外观品质自动分选装置软件V1.0"))
        
        self.groupBox_imageRegion.setTitle(_translate("MainWindow", "图像显示区域"))
        
        self.label_cameraImage_front.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">相机_正面</span></p></body></html>"))
        self.label_originalImage_front.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">原图_正面</span></p></body></html>"))
        self.label_diseaseImage_front.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">病害_正面</span></p></body></html>"))
        self.label_crackleImage_front.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">裂纹_正面</span></p></body></html>"))
        self.label_gradeImage_front.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">大小_正面</span></p></body></html>"))                                           
        
        self.label_cameraImage_back.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">相机_背面</span></p></body></html>"))
        self.label_originalImage_back.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">原图_背面</span></p></body></html>"))
        self.label_diseaseImage_back.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">病害_背面</span></p></body></html>"))
        self.label_crackleImage_back.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">裂纹_背面</span></p></body></html>"))
        self.label_gradeImage_back.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">大小_背面</span></p></body></html>"))                                            
        
        self.groupBox_controlRegion.setTitle(_translate("MainWindow", "命令控制区域"))                                            

        self.button_workingSpeed.setText(_translate("MainWindow", "工作速度"))
        self.button_openCamera.setText(_translate("MainWindow", "打开相机"))
        self.button_signalTrigger.setText(_translate("MainWindow", "开始检测"))
        self.button_initialWindow.setText(_translate("MainWindow", "初始窗口"))                                           
                                                    
        self.groupBox_resultRegion.setTitle(_translate("MainWindow", "结果显示与统计区域"))

        self.label_quantity.setText(_translate("MainWindow","数量"))
        self.label_proportion.setText(_translate("MainWindow","占比"))                                      
                                                    
        self.groupBox_disease.setTitle(_translate("MainWindow", "病害"))
        
        self.label_yesDisease.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">有病害</span></p></body></html>"))
        self.label_noDisease.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">非病害</span></p></body></html>"))
        
        self.label_yesDisease_Quantity.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>"))
        self.label_yesDisease_Proportion.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>"))    
        self.label_noDisease_Quantity.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>"))
        self.label_noDisease_Proportion.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>"))
   
        self.groupBox_crackle.setTitle(_translate("MainWindow", "裂纹"))                                            
        
        self.label_yesCrackle.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">有裂纹</span></p></body></html>"))
        self.label_noCrackle.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">非裂纹</span></p></body></html>"))
        
        self.label_yesCrackle_Quantity.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>"))
        self.label_yesCrackle_Proportion.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>"))    
        self.label_noCrackle_Quantity.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>"))
        self.label_noCrackle_Proportion.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>"))
                                                           
        self.groupBox_grade.setTitle(_translate("MainWindow", "等级"))                                            
        
        self.label_specialGrade.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">一级枣</span></p></body></html>"))
        self.label_firstGrade.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">二级枣</span></p></body></html>"))
        self.label_secondGrade.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">三级枣</span></p></body></html>"))
        self.label_thirdGrade.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">四级枣</span></p></body></html>"))
                                                    
        self.label_specialGrade_Quantity.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>"))
        self.label_specialGrade_Proportion.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>"))    
        self.label_firstGrade_Quantity.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>"))
        self.label_firstGrade_Proportion.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>"))
        self.label_secondGrade_Quantity.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>"))
        self.label_secondGrade_Proportion.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>"))
        self.label_thirdGrade_Quantity.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>"))
        self.label_thirdGrade_Proportion.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>"))
                                                                                            
    #  画方框
    def paintEvent(self, event):
   
        qp_label_image = QtGui.QPainter()
        qp_label_image.begin(self)
        qp_label_image.setPen(QtGui.QPen(QtCore.Qt.darkGray, 2, QtCore.Qt.SolidLine))
        qp_label_image.drawRect(35, 215, 1008, 150)
        qp_label_image.drawRect(35, 55, 1008, 150)
        qp_label_image.drawLine(237, 55, 237, 205)
        qp_label_image.drawLine(439, 55, 439, 205)
        qp_label_image.drawLine(641, 55, 641, 205)
        qp_label_image.drawLine(843, 55, 843, 205)
        qp_label_image.drawLine(237, 215, 237, 365)
        qp_label_image.drawLine(439, 215, 439, 365)
        qp_label_image.drawLine(641, 215, 641, 365)
        qp_label_image.drawLine(843, 215, 843, 365)
        qp_label_image.end()


        
        
    def workingSpeed(self):
        form1 = QtWidgets.QDialog()
        ui = Ui_MWindow()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.form.show()
    
    def openCamera(self, event):
        if self.timer_showCamera.isActive() == False:
            flag_front = self.cap_front.open(0)
            flag_back = self.cap_back.open(1)
            
            if flag_front == False or flag_back == False:
                yes = QtWidgets.QPushButton()
                yes.setText("确定")
                message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "请检测相机与树莓派是否正确连接！")
                message.addButton(yes, QtWidgets.QMessageBox.ActionRole)
                
                if message.exec_() == QtWidgets.QMessageBox.ActionRole:
                    event.accept()

            else:
                self.timer_showCamera.start(1)  # 开始一个1毫秒的定时器
                self.button_openCamera.setText("关闭相机")

        else:
            yes = QtWidgets.QPushButton()
            no = QtWidgets.QPushButton()
            yes.setText("确定")
            no.setText("取消")
            reply = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "关闭相机后窗口将清空！")
            reply.addButton(yes, QtWidgets.QMessageBox.ActionRole)
            reply.addButton(no, QtWidgets.QMessageBox.RejectRole)

            if reply.exec_() == QtWidgets.QMessageBox.RejectRole:
               False
            
            else:
               self.timer_showCamera.stop()  # 停止定时器
               self.cap_front.release()  # 释放摄像头
               self.cap_back.release()
               self.button_openCamera.setText("打开相机")
               self.label_cameraImage_front.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">相机_正面</span></p></body></html>")
               self.label_originalImage_front.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">原图_正面</span></p></body></html>")
               self.label_diseaseImage_front.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">病害_正面</span></p></body></html>")
               self.label_crackleImage_front.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">裂纹_正面</span></p></body></html>")
               self.label_gradeImage_front.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">大小_正面</span></p></body></html>")
               self.label_cameraImage_back.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">相机_背面</span></p></body></html>")
               self.label_originalImage_back.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">原图_背面</span></p></body></html>")
               self.label_diseaseImage_back.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">病害_背面</span></p></body></html>")
               self.label_crackleImage_back.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">裂纹_背面</span></p></body></html>")
               self.label_gradeImage_back.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">大小_背面</span></p></body></html>")
                           
    def showCamera(self):
        ret_front, self.frame_front = self.cap_front.read()  # 第一个参数ret的值为True或False，代表有没有读到图片；第二个参数是frame，是当前截取一帧的图片
        self.frame_front = cv2.resize(self.frame_front, (200, 150))  # 重新调整窗口大小并显示
        M = cv2.getRotationMatrix2D((100, 75), 180, 1.0)
        self.frame_front = cv2.warpAffine(self.frame_front, M, (200, 150))
        image_camera_front = cv2.cvtColor(self.frame_front, cv2.COLOR_BGR2RGB)  #图片从读取的BGR格式转换到显示的RGB格式
        image_camera_front = QtGui.QImage(image_camera_front.data, image_camera_front.shape[1], image_camera_front.shape[0], QtGui.QImage.Format_RGB888)  # 这里的shape[1]其实就是图像的宽，而shape[0]就是高
        self.label_cameraImage_front.setPixmap(QtGui.QPixmap.fromImage(image_camera_front))
        
        ret_back, self.frame_back = self.cap_back.read()
        self.frame_back = cv2.resize(self.frame_back, (200, 150))
        self.frame_back = cv2.warpAffine(self.frame_back, M, (200, 150))
        image_camera_back = cv2.cvtColor(self.frame_back, cv2.COLOR_BGR2RGB)  
        image_camera_back = QtGui.QImage(image_camera_back.data, image_camera_back.shape[1], image_camera_back.shape[0], QtGui.QImage.Format_RGB888)
        self.label_cameraImage_back.setPixmap(QtGui.QPixmap.fromImage(image_camera_back))

    def signalTrigger(self, event):
        if self.value_judgement == 0:
            if self.cap_front.isOpened() and self.cap_back.isOpened():
                self.button_signalTrigger.setText("停止检测")
                
                def callback_front(channel):
                    self.num_write += 1
                    cv2.imwrite("/home/pi/Desktop/Dateimage/%d.jpg"%(self.num_write), self.frame_front)
                    
                def callback_back(channel):
                    self.frame_back = cv2.resize(self.frame_back, (200, 150))
                    image_original_back = cv2.cvtColor(self.frame_back, cv2.COLOR_BGR2RGB)
                    image_original_back = QtGui.QImage(image_original_back.data, image_original_back.shape[1], image_original_back.shape[0], QtGui.QImage.Format_RGB888)
                    self.label_originalImage_back.setPixmap(QtGui.QPixmap.fromImage(image_original_back))
                    
                    self.gray_back = cv2.cvtColor(self.frame_back, cv2.COLOR_BGR2GRAY)
                    ret, self.thresh_back = cv2.threshold(self.gray_back, 27, 255, cv2.THRESH_BINARY_INV)
                    self.thresh = self.thresh_back
                    self.mediant_disease = 0
                    self.classification_disease()
                    
                    self.num_read += 1
                    self.image_front_read = cv2.imread("/home/pi/Desktop/Dateimage/%d.jpg"%(self.num_read))
                    self.image_front_read = cv2.resize(self.image_front_read, (200, 150))
                    image_original_front = cv2.cvtColor(self.image_front_read, cv2.COLOR_BGR2RGB)
                    image_original_front = QtGui.QImage(image_original_front.data, image_original_front.shape[1], image_original_front.shape[0], QtGui.QImage.Format_RGB888)
                    self.label_originalImage_front.setPixmap(QtGui.QPixmap.fromImage(image_original_front))
                    
                    '''self.image_front_read_path = "E:\Dateimage\colletion\hz%d.jpg"%(self.num_read)
                    os.remove(self.image_front_read_path)'''
                    
                    self.gray_front = cv2.cvtColor(self.image_front_read, cv2.COLOR_BGR2GRAY)
                    ret, self.thresh_front = cv2.threshold(self.gray_front, 27, 255, cv2.THRESH_BINARY_INV)
                    self.thresh = self.thresh_front
                    self.mediant_disease = 1
                    self.classification_disease()
                    
                    self.result_disease()
                
                # GPIO.setmode(GPIO.BOARD)
                # GPIO.setup(38, GPIO.IN)
                # GPIO.setup(39, GPIO.IN)
                # GPIO.add_event_detect(38, GPIO.FALLING, callback = callback_front, bouncetime = 200)
                # GPIO.add_event_detect(39, GPIO.FALLING, callback = callback_back, bouncetime = 200)
            
            else:
                yes = QtWidgets.QPushButton()
                yes.setText("确定")
                reply = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "提示", "请先打开相机！")
                reply.addButton(yes,QtWidgets.QMessageBox.ActionRole)
                     
                if reply.exec_() == QtWidgets.QMessageBox.ActionRole:
                    event.accept()
        else:
            yes = QtWidgets.QPushButton()
            no = QtWidgets.QPushButton()
            yes.setText("确定")
            no.setText("取消")
            reply = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "停止检测后停止工作！")
            reply.addButton(yes, QtWidgets.QMessageBox.ActionRole)
            reply.addButton(no, QtWidgets.QMessageBox.RejectRole)

            if reply.exec_() == QtWidgets.QMessageBox.RejectRole:
               False
            
            else:
               self.value_judgement = 0
               self.button_signalTrigger.setText("开始检测")
               self.label_originalImage_front.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">原图_正面</span></p></body></html>")
               self.label_diseaseImage_front.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">病害_正面</span></p></body></html>")
               self.label_crackleImage_front.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">裂纹_正面</span></p></body></html>")
               self.label_gradeImage_front.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">大小_正面</span></p></body></html>")
               self.label_originalImage_back.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">原图_背面</span></p></body></html>")
               self.label_diseaseImage_back.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">病害_背面</span></p></body></html>")
               self.label_crackleImage_back.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">裂纹_背面</span></p></body></html>")
               self.label_gradeImage_back.setText(
                       "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">大小_背面</span></p></body></html>")
                    
    def classification_disease(self):      
        erosionkerne_disease = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
        erosion_disease = cv2.erode(self.thresh, erosionkerne_disease)
        dilationkerne_disease = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 20))
        dilation_disease = cv2.dilate(erosion_disease, dilationkerne_disease)
        edges_disease = cv2.Canny(dilation_disease, 100, 100)
        image, contours_disease, hierarchy = cv2.findContours(edges_disease, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        number_contours = len(contours_disease)
            
        if contours_disease:
            if number_contours == 1:
                cnt = contours_disease[0]
                rect_disease = cv2.minAreaRect(cnt)
                 
            else:
                cnt = contours_disease[1]
                rect_disease = cv2.minAreaRect(cnt)
                
            x1, x2 = rect_disease[1]
                
            if x1 >= x2:
                length = x1
                width  = x2
            else:
                length = x2
                width  = x1

            (x,y),radius = cv2.minEnclosingCircle(cnt)  
            center = (int(x),int(y))  
            radius = int(radius) 
            thresh_disease = cv2.cvtColor(self.thresh, cv2.COLOR_GRAY2BGR)
            
            if (width >= 25 and width <= 60 and length >= 1 * width and length <= 2 * width):
                if self.mediant_disease == 0:
                    self.label_gradeImage_back.clear()
                    self.label_crackleImage_back.clear()
                else:
                    self.label_gradeImage_front.clear()
                    self.label_crackleImage_front.clear()
                
                image_yesDisease = cv2.circle(thresh_disease, center, radius, (0,255,0),2)  
                image_yesDisease = cv2.cvtColor(image_yesDisease, cv2.COLOR_BGR2RGB)
                image_yesDisease = QtGui.QImage(image_yesDisease.data, image_yesDisease.shape[1], image_yesDisease.shape[0], QtGui.QImage.Format_RGB888)
                image_yesDisease = QtGui.QPixmap.fromImage(image_yesDisease)
                
                if self.mediant_disease == 0:
                    self.label_diseaseImage_back.setPixmap(image_yesDisease)
                    self.yesDisease_back = 1
                else:
                    self.label_diseaseImage_front.setPixmap(image_yesDisease)
                    self.yesDisease_front = 1
            
            else:
                image_noDisease = cv2.circle(thresh_disease,center,radius,(0,0,255),2)
                image_noDisease = cv2.cvtColor(image_noDisease, cv2.COLOR_BGR2RGB)
                image_noDisease = QtGui.QImage(image_noDisease.data, image_noDisease.shape[1], image_noDisease.shape[0], QtGui.QImage.Format_RGB888)
                image_noDisease = QtGui.QPixmap.fromImage(image_noDisease)
                if self.mediant_disease == 0:
                    self.label_diseaseImage_back.setPixmap(image_noDisease)
                    self.yesDisease_back = 0
                else:
                    self.label_diseaseImage_front.setPixmap(image_noDisease)
                    self.yesDisease_front = 0
                   
        else:
            image_noDisease_noDefect = cv2.cvtColor(dilation_disease, cv2.COLOR_GRAY2RGB)
            image_noDisease_noDefect = QtGui.QImage(image_noDisease_noDefect.data, image_noDisease_noDefect.shape[1], image_noDisease_noDefect.shape[0], QtGui.QImage.Format_RGB888)
            image_noDisease_noDefect = QtGui.QPixmap.fromImage(image_noDisease_noDefect)
            if self.mediant_disease == 0:
                self.label_diseaseImage_back.setPixmap(image_noDisease_noDefect)
                self.yesDisease_back = 0
            else:
                self.lable_diseaseImage_front.setPixmap(image_noDisease_noDefect)
                self.yesDisease_front = 0
            
    def result_disease(self):
        if self.yesDisease_front == 1 or self.yesDisease_back == 1:
            self.label_yesDisease.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">有病害</span></p></body></html>")   
            self.label_noDisease.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">无病害</span></p></body></html>")
            self.SUM_yesDisease += 1
            self.label_yesDisease_Quantity.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">%d</span></p></body></html>" % self.SUM_yesDisease)
                
        else:
            self.label_noDisease.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">无病害</span></p></body></html>")
            self.label_yesDisease.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">有病害</span></p></body></html>")
            self.SUM_noDisease += 1
            self.label_noDisease_Quantity.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">%d</span></p></body></html>" % self.SUM_noDisease)
            
            self.thresh = self.thresh_back
            self.mediant_crackle = 0
            self.classification_crackle()
            
            self.thresh = self.thresh_front
            self.mediant_crackle = 1
            self.classification_crackle()
            self.result_crackle()
            
        SUM_disease = self.SUM_yesDisease + self.SUM_noDisease
        PROP_yesDisease = (self.SUM_yesDisease / SUM_disease) * 100
        PROP_noDisease = (self.SUM_noDisease / SUM_disease) * 100
            
        self.label_yesDisease_Proportion.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">%.1f%%</span></p></body></html>" % PROP_yesDisease)
        self.label_noDisease_Proportion.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">%.1f%%</span></p></body></html>" % PROP_noDisease)
                    
    def classification_crackle(self):
        dilationkerne_crackle = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (40, 15))
        dilation_crackle = cv2.dilate(self.thresh, dilationkerne_crackle)
        edges_crackle = cv2.Canny(dilation_crackle, 100, 100)
        image, contours_crackle, hierarchy = cv2.findContours(edges_crackle, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours_crackle:
            rect_crackle = cv2.minAreaRect(contours_crackle[0])
            x1, x2 = rect_crackle[1]
                
            if x1 >= x2:
                length = x1
                width  = x2
            else:
                length = x2
                width  = x1
                
            box = cv2.boxPoints(rect_crackle)
            thresh_crackle = cv2.cvtColor(self.thresh, cv2.COLOR_GRAY2BGR)
            box = np.int0(box)
                
            if (width >= 15 and length >= 2.4 * width) or (length >= 80):
                if self.mediant_crackle == 0:
                    self.label_gradeImage_back.clear()
                else:
                    self.label_gradeImage_front.clear()
                    
                cv2.drawContours(thresh_crackle, [box], 0, (0, 255, 0), 2)
                image_yesCrackle = cv2.cvtColor(thresh_crackle, cv2.COLOR_BGR2RGB)
                image_yesCrackle = QtGui.QImage(image_yesCrackle.data, image_yesCrackle.shape[1], image_yesCrackle.shape[0], QtGui.QImage.Format_RGB888)
                image_yesCrackle = QtGui.QPixmap.fromImage(image_yesCrackle)
                
                if self.mediant_crackle == 0:
                    self.label_crackleImage_back.setPixmap(image_yesCrackle)
                    self.yesCrackle_back = 1
                else:   
                    self.label_crackleImage_front.setPixmap(image_yesCrackle)
                    self.yesCrackle_front = 1
                         
            else:
                cv2.drawContours(thresh_crackle, [box], 0, (0, 0, 255), 2)
                image_noCrackle = cv2.cvtColor(thresh_crackle, cv2.COLOR_BGR2RGB)
                image_noCrackle = QtGui.QImage(image_noCrackle.data, image_noCrackle.shape[1], image_noCrackle.shape[0], QtGui.QImage.Format_RGB888)
                image_noCrackle = QtGui.QPixmap.fromImage(image_noCrackle)
                
                if self.mediant_crackle == 0:
                    self.label_crackleImage_back.setPixmap(image_noCrackle)
                    self.yesCrackle_back = 0
                else:
                    self.label_crackleImage_front.setPixmap(image_noCrackle)
                    self.yesCrackle_front = 0
       
        else:
            image_noCrackle_noDefect = cv2.cvtColor(dilation_crackle, cv2.COLOR_GRAY2RGB)
            image_noCrackle_noDefect = QtGui.QImage(image_noCrackle_noDefect.data, image_noCrackle_noDefect.shape[1], image_noCrackle_noDefect.shape[0], QtGui.QImage.Format_RGB888)
            image_noCrackle_noDefect = QtGui.QPixmap.fromImage(image_noCrackle_noDefect)
            if self.mediant_crackle == 0:
                self.label_crackleImage_back.setPixmap(image_noCrackle_noDefect)
                self.yesCrackle_back = 0
            else:
                self.label_crackleImage_front.setPixmap(image_noCrackle_noDefect)
                self.yesCrackle_front = 0
            
    def result_crackle(self):
        if self.yesCrackle_back == 1 or self.yesCrackle_front == 1:
            self.label_yesCrackle.setText(
                        "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">有裂纹</span></p></body></html>")     
            self.label_noCrackle.setText(
                        "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">无裂纹</span></p></body></html>")            
            self.SUM_yesCrackle += 1
            self.label_yesCrackle_Quantity.setText(
                        "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">%d</span></p></body></html>" % self.SUM_yesCrackle)
        else:
            self.label_noCrackle.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">无裂纹</span></p></body></html>")
            self.label_yesCrackle.setText(
                        "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">有裂纹</span></p></body></html>")
            self.SUM_noCrackle += 1
            self.label_noCrackle_Quantity.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">%d</span></p></body></html>" % self.SUM_noCrackle)
        
            self.gray = self.gray_back
            self.mediant_grade = 0
            self.classification_grade()
            
            self.gray = self.gray_front
            self.mediant_grade = 1
            self.classification_grade()
            
            self.result_grade()
        
        SUM_crackle = self.SUM_yesCrackle + self.SUM_noCrackle
        PROP_yesCrackle = (self.SUM_yesCrackle / SUM_crackle) * 100
        PROP_noCrackle = (self.SUM_noCrackle / SUM_crackle) * 100
            
        self.label_yesCrackle_Proportion.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">%.1f%%</span></p></body></html>" % PROP_yesCrackle)
        self.label_noCrackle_Proportion.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">%.1f%%</span></p></body></html>" % PROP_noCrackle)
    
    def classification_grade(self):   
        ret, thresh_grade = cv2.threshold(self.gray, 0, 255, cv2.THRESH_OTSU)  # OTSU阈值处理成二值化图
        ret, thresh_grade = cv2.threshold(thresh_grade, 100, 255, cv2.THRESH_BINARY_INV)  # 颜色反转
        erosionkerne_grade = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (12, 12))
        erosion_grade = cv2.erode(thresh_grade, erosionkerne_grade)
        dilationkerne_grade = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
        dilation_grade = cv2.dilate(erosion_grade, dilationkerne_grade)

        image_Grade, contours_Grade, hierarchy = cv2.findContours(dilation_grade, 3, 2) # 寻找轮廓
        hull = cv2.convexHull(contours_Grade[0]) # 检测第一个轮廓是否具有凸性缺陷，并能纠正缺陷
        image_Grade = cv2.cvtColor(image_Grade, cv2.COLOR_GRAY2BGR) # 色彩变换
        image_Grade = cv2.polylines(image_Grade, [hull], True, (0, 255, 0), 2) # 根据轮廓画凸包
        image_Grade = cv2.fillPoly(image_Grade, np.int_([hull]), (255, 255, 255))   # 将凸包内部填充白色
        
        image_grade = cv2.cvtColor(image_Grade, cv2.COLOR_BGR2RGB) # 色彩变换
        image_grade = QtGui.QImage(image_grade.data, image_grade.shape[1], image_grade.shape[0], QtGui.QImage.Format_RGB888)
        image_grade = QtGui.QPixmap.fromImage(image_grade)

        if self.mediant_grade == 0:
            self.label_gradeImage_back.setPixmap(image_grade) 
            image_grade_filling = cv2.cvtColor(image_Grade, cv2.COLOR_BGR2GRAY)
            self.number_whitepixel_back = cv2.countNonZero(image_grade_filling)
        
        else:
            self.label_gradeImage_front.setPixmap(image_grade)
            image_grade_filling = cv2.cvtColor(image_Grade, cv2.COLOR_BGR2GRAY)
            self.number_whitepixel_front = cv2.countNonZero(image_grade_filling)
        
    def result_grade(self):
        # 根据白色像素点数量进行分级
        averageNumber_whitepixel = (self.number_whitepixel_back + self.number_whitepixel_front)/2
        if averageNumber_whitepixel  >= 7000:  # 特级枣
            self.label_specialGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">特级枣</span></p></body></html>")
            self.label_firstGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">一级枣</span></p></body></html>")
            self.label_secondGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">二级枣</span></p></body></html>")
            self.label_thirdGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">三级枣</span></p></body></html>")
            self.SUM_specialGrade += 1
            self.label_specialGrade_Quantity.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">%d</span></p></body></html>" % self.SUM_specialGrade)

        elif averageNumber_whitepixel > 6000 and averageNumber_whitepixel <= 7000:  # 一级枣
            self.label_firstGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">一级枣</span></p></body></html>")
            self.label_specialGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">特级枣</span></p></body></html>")
            self.label_secondGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">二级枣</span></p></body></html>")            
            self.label_thirdGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">三级枣</span></p></body></html>")            
            self.SUM_firstGrade += 1
            self.label_firstGrade_Quantity.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">%d</span></p></body></html>" % self.SUM_firstGrade)
        
        elif averageNumber_whitepixel > 5000 and averageNumber_whitepixel <= 6000:  # 二级枣
            self.label_secondGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">二级枣</span></p></body></html>")
            self.label_specialGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">特级枣</span></p></body></html>")
            self.label_firstGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">一级枣</span></p></body></html>")
            self.label_thirdGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">三级枣</span></p></body></html>")            
            self.SUM_secondGrade += 1
            self.label_secondGrade_Quantity.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">%d</span></p></body></html>" % self.SUM_secondGrade)                
                        
        else:  # 三级枣
            self.label_thirdGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">三级枣</span></p></body></html>")
            self.label_specialGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">特级枣</span></p></body></html>")
            self.label_firstGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">一级枣</span></p></body></html>")
            self.label_secondGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">二级枣</span></p></body></html>")            
            self.SUM_thirdGrade += 1
            self.label_thirdGrade_Quantity.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">%d</span></p></body></html>" %self.SUM_thirdGrade)

        SUM_grade = self.SUM_specialGrade + self.SUM_firstGrade + self.SUM_secondGrade + self.SUM_thirdGrade
        PROP_specialGrade = (self.SUM_specialGrade / SUM_grade) * 100
        PROP_firstGrade = (self.SUM_firstGrade / SUM_grade) * 100
        PROP_secondGrade = (self.SUM_secondGrade / SUM_grade) * 100
        PROP_thirdGrade = (self.SUM_thirdGrade / SUM_grade) * 100

        self.label_specialGrade_Proportion.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">%.1f%%</span></p></body></html>" % PROP_specialGrade)
        self.label_firstGrade_Proportion.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">%.1f%%</span></p></body></html>" % PROP_firstGrade)
        self.label_secondGrade_Proportion.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">%.1f%%</span></p></body></html>" % PROP_secondGrade)
        self.label_thirdGrade_Proportion.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">%.1f%%</span></p></body></html>" % PROP_thirdGrade) 
      
    def initialWindow(self, event):
        yes = QtWidgets.QPushButton()
        no = QtWidgets.QPushButton()
        yes.setText("确定")
        no.setText("取消")
        reply = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "初始窗口后所有数据将清空！")
        reply.addButton(yes, QtWidgets.QMessageBox.ActionRole)
        reply.addButton(no, QtWidgets.QMessageBox.RejectRole)

        if reply.exec_() == QtWidgets.QMessageBox.RejectRole:
            False
            
        else:
            self.timer_showCamera.stop()
            self.cap_front.release()
            self.cap_back.release()
            self.button_openCamera.setText("打开相机")
            self.label_cameraImage_front.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">相机_正面</span></p></body></html>")
            self.label_originalImage_front.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">原图_正面</span></p></body></html>")
            self.label_diseaseImage_front.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">病害_正面</span></p></body></html>")
            self.label_crackleImage_front.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">裂纹_正面</span></p></body></html>")
            self.label_gradeImage_front.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">大小_正面</span></p></body></html>")
            self.label_cameraImage_back.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">相机_背面</span></p></body></html>")
            self.label_originalImage_back.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">原图_背面</span></p></body></html>")
            self.label_diseaseImage_back.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">病害_背面</span></p></body></html>")
            self.label_crackleImage_back.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">裂纹_背面</span></p></body></html>")
            self.label_gradeImage_back.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">大小_背面</span></p></body></html>")
            
            self.label_yesDisease.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">有病害</span></p></body></html>")
            self.label_noDisease.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">非病害</span></p></body></html>")
            self.label_yesCrackle.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">有裂纹</span></p></body></html>")
            self.label_noCrackle.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">非裂纹</span></p></body></html>")
            self.label_specialGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">特等枣</span></p></body></html>")
            self.label_firstGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">一等枣</span></p></body></html>")
            self.label_secondGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">二等枣</span></p></body></html>")
            self.label_thirdGrade.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:400;color:#000000;\">三等枣</span></p></body></html>") 
             
            self.num_write = 0
            self.num_read = 0
            self.yesDisease_front = 0
            self.yesDisease_back = 0
            self.yesCrackle_front = 0
            self.yesCrackle_back = 0
            self.SUM_yesDisease = 0
            self.SUM_noDisease = 0
            self.SUM_yesCrackle = 0
            self.SUM_noCrackle = 0
            self.SUM_specialGrade = 0
            self.SUM_firstGrade = 0
            self.SUM_secondGrade = 0
            self.SUM_thirdGrade = 0
            
            self.label_yesDisease_Quantity.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>")
            self.label_yesDisease_Proportion.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>")    
            self.label_noDisease_Quantity.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>")
            self.label_noDisease_Proportion.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>")
            self.label_yesCrackle_Quantity.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>")
            self.label_yesCrackle_Proportion.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>")    
            self.label_noCrackle_Quantity.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>")
            self.label_noCrackle_Proportion.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>")
            self.label_specialGrade_Quantity.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>")
            self.label_specialGrade_Proportion.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>")    
            self.label_firstGrade_Quantity.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>")
            self.label_firstGrade_Proportion.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>")
            self.label_secondGrade_Quantity.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>")
            self.label_secondGrade_Proportion.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>")    
            self.label_thirdGrade_Quantity.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>")
            self.label_thirdGrade_Proportion.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-weight:500;color:#ff0000;\">0</span></p></body></html>")
                    
    def closeEvent(self, event):
        yes = QtWidgets.QPushButton()
        no = QtWidgets.QPushButton()
        yes.setText("确定")
        no.setText("取消")
        reply = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "退出后测试将停止,\n你确认要退出吗？")
        reply.addButton(yes,QtWidgets.QMessageBox.ActionRole)
        reply.addButton(no, QtWidgets.QMessageBox.RejectRole)
    
        if reply.exec_() == QtWidgets.QMessageBox.RejectRole:
            event.ignore()
        else:
            event.accept()
            self.cap_front.release()
            self.cap_back.release()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())