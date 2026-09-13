import sys
from PyQt5.QtWidgets import QWidget, QGridLayout,QPushButton,QLineEdit,QApplication,QStyleFactory
from PyQt5.QtCore import Qt
class calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.lineedit=QLineEdit(self)
        self.btn_enter=QPushButton("Enter",self)
        self.btn_clear=QPushButton("Clear",self)
        self.btn_9=QPushButton("9",self)
        self.btn_8=QPushButton("8",self)
        self.btn_7=QPushButton("7",self)
        self.btn_add=QPushButton("+",self)
        self.btn_6=QPushButton("6",self)
        self.btn_5=QPushButton("5",self)
        self.btn_4=QPushButton("4",self)
        self.btn_min=QPushButton("-",self)
        self.btn_3=QPushButton("3",self)
        self.btn_2=QPushButton("2",self)
        self.btn_1=QPushButton("1",self)
        self.btn_mul=QPushButton("*",self)
        self.btn_0=QPushButton("0",self)
        self.btn_div=QPushButton("÷",self)
        self.temp_numbs=[]
        self.fin_numbs=[]
        self.store_ans=[]
        self.just_calculated=False
        self.initUI()
    def initUI(self):
        self.gridlayout=QGridLayout()
        self.gridlayout.addWidget(self.lineedit,0,0,1,4)
        self.gridlayout.addWidget(self.btn_enter,1,0,1,2)
        self.gridlayout.addWidget(self.btn_clear,1,2,1,2)
        self.gridlayout.addWidget(self.btn_9,2,0)
        self.gridlayout.addWidget(self.btn_8,2,1)
        self.gridlayout.addWidget(self.btn_7,2,2)
        self.gridlayout.addWidget(self.btn_add,2,3)
        self.gridlayout.addWidget(self.btn_6,3,0)
        self.gridlayout.addWidget(self.btn_5,3,1)
        self.gridlayout.addWidget(self.btn_4,3,2)
        self.gridlayout.addWidget(self.btn_min,3,3)
        self.gridlayout.addWidget(self.btn_3,4,0)
        self.gridlayout.addWidget(self.btn_2,4,1)
        self.gridlayout.addWidget(self.btn_1,4,2)
        self.gridlayout.addWidget(self.btn_mul,4,3)
        self.gridlayout.addWidget(self.btn_0,5,0,1,3)
        self.gridlayout.addWidget(self.btn_div,5,3)
        self.setLayout(self.gridlayout)
        self.btn_enter.clicked.connect(self.func_result)
        self.btn_clear.clicked.connect(self.clear_cal)
        self.btn_9.clicked.connect(lambda: self.num_press('9'))
        self.btn_8.clicked.connect(lambda: self.num_press('8'))   
        self.btn_7.clicked.connect(lambda: self.num_press('7'))
        self.btn_6.clicked.connect(lambda: self.num_press('6'))
        self.btn_5.clicked.connect(lambda: self.num_press('5'))
        self.btn_4.clicked.connect(lambda: self.num_press('4'))
        self.btn_3.clicked.connect(lambda: self.num_press('3'))
        self.btn_2.clicked.connect(lambda: self.num_press('2'))
        self.btn_1.clicked.connect(lambda: self.num_press('1'))
        self.btn_0.clicked.connect(lambda: self.num_press('0'))
        self.btn_add.clicked.connect(lambda: self.operator_press('+'))
        self.btn_min.clicked.connect(lambda: self.operator_press('-'))
        self.btn_mul.clicked.connect(lambda: self.operator_press('*'))
        self.btn_div.clicked.connect(lambda: self.operator_press('/'))
    def num_press(self,number):
        self.just_calculated=False
        if self.store_ans:
            self.store_ans=[]
            self.fin_numbs=[]
            self.temp_numbs=[]
        self.temp_numbs.append(number)
        temp_string=''.join(self.temp_numbs)
        if self.fin_numbs:
            self.lineedit.setText(''.join(self.fin_numbs)+temp_string)
        else:
            self.lineedit.setText(temp_string)
    def operator_press(self,operator):
        self.just_calculated=False
        if self.store_ans:
            self.fin_numbs.append(self.store_ans[0])
            self.fin_numbs.append(operator)
            self.temp_numbs=[]
            self.store_ans=[]
            self.lineedit.setText(''.join(self.fin_numbs))
            return
        if not self.temp_numbs and not self.fin_numbs:
            self.fin_numbs.append('0')
            self.fin_numbs.append(operator)
            self.lineedit.setText(''.join(self.fin_numbs))
            return
        if not self.temp_numbs:
            return
        temp_string=''.join(self.temp_numbs)
        self.fin_numbs.append(temp_string)
        self.fin_numbs.append(operator)
        self.temp_numbs=[]
        self.lineedit.setText(''.join(self.fin_numbs))
    def func_result(self):
        if self.just_calculated:
            return
        fin_string=''.join(self.fin_numbs)+''.join(self.temp_numbs)
        if self.store_ans:
            fin_string=''.join(self.store_ans)+''.join(self.temp_numbs)
        if not fin_string:
            return
        if self.fin_numbs and self.fin_numbs[-1] in ["+","-","*","/"] and not self.temp_numbs:
            return
        try:
            result_string=eval(fin_string)
            if result_string==int(result_string):
                result_string=int(result_string)
        except ZeroDivisionError:
            self.lineedit.setText("Math error")
            return
        fin_string+='='
        fin_string+=str(result_string)
        self.store_ans=[str(result_string)]
        self.temp_numbs=[]
        self.fin_numbs=[]
        self.lineedit.setText(fin_string)
        self.just_calculated=True
    def clear_cal(self):
        self.lineedit.clear()
        self.temp_numbs=[]
        self.fin_numbs=[]
        self.store_ans=[]
        self.just_calculated=False
if __name__== '__main__':
    app=QApplication(sys.argv)
    calcu_lator=calculator()
    calcu_lator.show()
    app.setStyle(QStyleFactory.create('Fusion'))
    sys.exit(app.exec_())
   