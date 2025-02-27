import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, 
QVBoxLayout,QHBoxLayout,QGridLayout, QPushButton, QCheckBox)
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Calculator")
        self.setGeometry((1920-400) / 2, (1080-600) / 2, 400, 600)
        self.setWindowIcon(QIcon("assets/calcIcon.png"))

        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.numberButtons = [QPushButton(str(x),self) for x in range(0,10)]

        for x in range(0,10):
            self.numberButtons[x].clicked.connect(lambda checked,x=x: on_click(self,x))

        hbox_top = QHBoxLayout()
        hbox_mid = QHBoxLayout()
        hbox_bot = QHBoxLayout()
        vbox = QVBoxLayout()

        for x in range(7,10):
            hbox_top.addWidget(self.numberButtons[x])

        for x in range(4,7):
            hbox_mid.addWidget(self.numberButtons[x])

        for x in range(1,4):
            hbox_bot.addWidget(self.numberButtons[x])
        
        vbox.addLayout(hbox_top)
        vbox.addLayout(hbox_mid)
        vbox.addLayout(hbox_bot)

        central_widget.setLayout(vbox)

        def on_click(self,value):
            print (value + 1)

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