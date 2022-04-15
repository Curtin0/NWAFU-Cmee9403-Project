import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

class MainWindow(QWidget):
    
    def __init__(self, subWindow):
        
        super().__init__()
        self.subWindow = subWindow
        self.initUI()
    
    def initUI(self):
        
        btn = QPushButton('显示子界面', self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('主界面')
        self.show()
        
        btn.clicked.connect(self.openSubWindow)

    def openSubWindow(self):

    	self.subWindow.show()


class SubWindow(QWidget):
    
    def __init__(self, subWindow):
        
        super().__init__()
        self.subWindow = subWindow
        self.initUI()
    
    def initUI(self):

        btn = QPushButton('显示二级子界面', self)
        btn.clicked.connect(self.openSubWindow)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        
        self.setGeometry(350, 350, 250, 150)
        self.setWindowTitle('子界面')
        
    def openSubWindow(self):

    	self.subWindow.show()

class SubSubWindow(QWidget):
    
    def __init__(self):

        super().__init__()
        self.initUI()
    
    
    def initUI(self):

        self.setGeometry(400, 400, 250, 150)
        self.setWindowTitle('二级子界面')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    subSubWindow = SubSubWindow()
    subWindow = SubWindow(subSubWindow)
    mainWindow = MainWindow(subWindow)
    
    sys.exit(app.exec_())
