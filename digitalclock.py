import sys
from PyQt5.QtWidgets import QApplication,QVBoxLayout,QWidget,QLabel
from PyQt5.QtCore import Qt,QTimer,QTime
from PyQt5.QtGui import QFont,QFontDatabase
class digital_clock(QWidget):
   def __init__(self):
        super(). __init__()
        self.label=QLabel(self)
        self.timer=QTimer(self)
        self.initUI()
   def initUI(self):
        #self.setGeometry(700,300,500,500)
        self.setWindowTitle("Digital Clock by Anuj!")
        self.setStyleSheet("background-color:black;")
        self.label.setStyleSheet("color: red;" 
                                )
        font_id=QFontDatabase.addApplicationFont("DS-DIGI.TTF")
        font_family=QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font=QFont(font_family,100)
        self.label.setFont(my_font)
        vbox=QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.setAlignment(Qt.AlignCenter)
        self.setLayout(vbox)
        self.timer.timeout.connect(self.run_clock)
        self.timer.start(1000)
   def run_clock(self):
        currentime=QTime.currentTime().toString("hh:mm:ss:AP")
        self.label.setText(currentime)
if __name__== "__main__":
  app=QApplication(sys.argv)
  digitalclock=digital_clock()
  digitalclock.show()
  sys.exit(app.exec_())

  