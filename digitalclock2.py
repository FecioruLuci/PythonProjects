import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QHBoxLayout
from PyQt5.QtCore import QTimer, Qt
import datetime


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MydigitalClock")
        self.setGeometry(100,100,700,150)
        self.acuma = QTimer()
        self.acuma.timeout.connect(self.update_time)
        self.acuma.start(1000)
        self.label1 = QLabel("")
        self.update_time()
        self.initUI()



    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()
        hbox.addWidget(self.label1)
        central_widget.setLayout(hbox)
        self.setStyleSheet("background-color: black;")
        self.label1.setStyleSheet("font-size: 150px;"
        "font-family: Arial;"
        "color: hsl(4, 0%, 63%);")

    def update_time(self):
        acu = datetime.datetime.now().strftime("%H:%M:%S")
        ora = int(datetime.datetime.now().strftime("%H"))
        if ora > 12:
            acu = acu + "pm"
        else:
            acu = acu + "am"


        self.label1.setText(acu)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())