from PyQt5 import QtCore, QtWidgets, QtGui

class Ui_MainWindow(object):  # 新建一个类Ui_MainWindow继承object的属性
    def setupUi(self, MainWindow):
        # 新建窗体，建标签、按钮
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(QtCore.QRect(180, 100, 1080, 700))
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