import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, 
QVBoxLayout,QHBoxLayout,QGridLayout, QPushButton, QCheckBox, QSizePolicy)
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt

#--------- N A M I N G _ C O N V E N T I O N ---------------
# Variables: var_name
# Functions: funcName
# Classes/Objects: VarName
#--------- N A M I N G _ C O N V E N T I O N ---------------

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Calculator")
        self.setGeometry((1920-400) / 2, (1080-600) / 2, 400, 600)
        self.setWindowIcon(QIcon("assets/calcIcon.png"))
        self.setStyleSheet("background-color: gray;")

        self.initUI()
    
    def initUI(self):
        self.current_value = 0
        self.previous_value = 0
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.textLabel = QLabel(str(self.current_value),self)
        self.textLabel.setFont(QFont("Impact",35))
        self.textLabel.setStyleSheet("background-color: green;"
        "padding-right: 1 px;")
        self.textLabel.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.textLabel.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.numberButtons = [QPushButton(str(x),self) for x in range(0,10)]

        self.operationsButtons = [QPushButton(x,self) for x in ['+','-','X','/','ENTER','CLEAR']]

        for x in range(0,10):
            self.numberButtons[x].setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
            self.numberButtons[x].setStyleSheet("background-color: white;")
            self.numberButtons[x].clicked.connect(lambda checked,x=x: on_click_numbers(self,x))

        for x in range(len(self.operationsButtons)):
            self.operationsButtons[x].setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
            self.operationsButtons[x].setStyleSheet("background-color: white;")
            self.operationsButtons[x].clicked.connect(lambda checked,x=x: on_click_numbers(self,x))

        gridLayout = QGridLayout()

        gridLayout.addWidget(self.textLabel,0,0,1,5)

        for row in range(3):
            for col in range(3):
                val = 3*row + col + 3 - (col * 2)
                gridLayout.addWidget(self.numberButtons[10 - val],row+1,col)

        gridLayout.addWidget(self.operationsButtons[0],1,3)
        gridLayout.addWidget(self.operationsButtons[1],1,4)
        gridLayout.addWidget(self.operationsButtons[2],2,3)
        gridLayout.addWidget(self.operationsButtons[3],2,4)
        gridLayout.addWidget(self.operationsButtons[4],3,3,2,1)
        gridLayout.addWidget(self.operationsButtons[5],3,4,2,1)

        gridLayout.addWidget(self.numberButtons[0],4,0,1,3)
        centralWidget.setLayout(gridLayout)

        def on_click_numbers(self,value):
            self.current_value = (self.current_value * 10) + value
            self.textLabel.setText(str(self.current_value))

        def on_click_operations(self):
            pass

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


    #     label = QLabel("MY CALCULATOR",self)
    #     label.setFont(QFont("Impact",35))
    #     #label.setGeometry(0,0,self.width(),100)
    #     label.setStyleSheet("background-color: green;")

    #     #label.setAlignment(Qt.AlignTop | Qt.AlignRight)
    #     label.setAlignment(Qt.AlignCenter)

    #     imgLabel = QLabel(self)
    #     #imgLabel.setGeometry(0,105,self.width(),250)

    #     pixmap = QPixmap("assets/calcIcon.png")
    #     imgLabel.setPixmap(pixmap)
    #     imgLabel.setScaledContents(True)

    #     self.bottomLabel = QLabel("Bottom Text")
    #     self.bottomLabel.setFont(QFont("Impact",35))
    #     self.bottomLabel.setStyleSheet("background-color: green;")
    #     self.bottomLabel.setAlignment(Qt.AlignCenter)

    #     self.button = QPushButton("Click Me!",self)
    #     self.button.clicked.connect(self.on_click)


    #     vbox = QVBoxLayout()

    #     vbox.addWidget(label)
    #     vbox.addWidget(imgLabel)
    #     vbox.addWidget(self.bottomLabel)
    #     vbox.addWidget(self.button)

    #     central_widget.setLayout(vbox)

    # def on_click(self):
    #     print("Clicked Button! Yay!!")
    #     self.bottomLabel.setText("Clicked!!!")