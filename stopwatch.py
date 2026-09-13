import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QHBoxLayout,QVBoxLayout
from PyQt5.QtCore import Qt,QTime,QTimer
class stopwatch(QWidget):
    def __init__(self):
        super(). __init__()
        self.time=QTime(0,0,0,0)
        self.setWindowTitle("Stopwatch by Anuj!")
        self.label=QLabel("00:00:00.00",self)
        self.button1=QPushButton("Start",self)
        self.button2=QPushButton("Stop",self)
        self.button3=QPushButton("Reset",self)
        self.timer=QTimer()
        self.initUI()
    def initUI(self):
        vbox=QVBoxLayout()
        vbox.addWidget(self.label)
        self.label.setAlignment(Qt.AlignCenter)
        hbox=QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setStyleSheet("""
                           QPushButton,QLabel{
                           padding:20px 30px;
                           font-weight: bold; 
                           font-family: calibri;}
                           QPushButton{
                           font-size: 50px;}
                           QLabel{
                           background-color: hsl(286, 42%, 57%);
                           border-radius:10px;
                           font-size: 80px;}
        """)
        self.button1.clicked.connect(self.start)
        self.button2.clicked.connect(self.stop)
        self.button3.clicked.connect(self.reset)
        self.timer.timeout.connect(self.displayscreen)

    def start(self):
        self.timer.start(10)
    def stop(self):
        self.timer.stop()
    def reset(self):
        self.timer.stop()
        self.time=QTime(0,0,0,0)
        self.label.setText(self.format_time(self.time))
    def displayscreen(self):
        self.time=self.time.addMSecs(10)
        self.label.setText(self.format_time(self.time))
    def format_time(self,time):
        hours=time.hour()
        minutes=time.minute()
        seconds=time.second()
        milliseconds=time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
if __name__=="__main__":
        app=QApplication(sys.argv)
        stop_watch=stopwatch()
        stop_watch.show()
        sys.exit(app.exec_())
                
