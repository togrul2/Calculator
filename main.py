import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from calculator import Ui_MainWindow as calculator_ui


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = calculator_ui()
        self.ui.setupUi(self)

        #Text bar
        self.ui.output_field.setReadOnly(True)
        self.ui.output_field.setPlainText('0')
        self.ui.output_field.setAlignment(QtCore.Qt.AlignRight)
        self.ui.output_field.setFont(QtGui.QFont('sans-serif', 20))
        self.text = self.ui.output_field.toPlainText()
        self.calculate = self.ui.output_field.toPlainText()

        # Button click event handlers
        self.ui.key_0.clicked.connect(lambda: self.key_num_clicked('0'))
        self.ui.key_1.clicked.connect(lambda: self.key_num_clicked('1'))
        self.ui.key_2.clicked.connect(lambda: self.key_num_clicked('2'))
        self.ui.key_3.clicked.connect(lambda: self.key_num_clicked('3'))
        self.ui.key_4.clicked.connect(lambda: self.key_num_clicked('4'))
        self.ui.key_5.clicked.connect(lambda: self.key_num_clicked('5'))
        self.ui.key_6.clicked.connect(lambda: self.key_num_clicked('6'))
        self.ui.key_7.clicked.connect(lambda: self.key_num_clicked('7'))
        self.ui.key_8.clicked.connect(lambda: self.key_num_clicked('8'))
        self.ui.key_9.clicked.connect(lambda: self.key_num_clicked('9'))

        self.ui.key_dot.clicked.connect(self.key_dot_Clicked)

        self.ui.key_add.clicked.connect(lambda: self.key_oper_Clicked('+'))
        self.ui.key_substract.clicked.connect(lambda: self.key_oper_Clicked('-'))
        self.ui.key_multiply.clicked.connect(lambda: self.key_oper_Clicked('*'))
        self.ui.key_divide.clicked.connect(lambda: self.key_oper_Clicked('/'))

        self.ui.key_calc.clicked.connect(self.key_calc_Clicked)
        self.ui.key_clear.clicked.connect(self.key_clear_Clicked)
        self.ui.key_bs.clicked.connect(self.key_bs_Clicked)
        self.ui.key_change_sign.clicked.connect(self.key_csign_Clicked)

    def keyPressEvent(self, event):
        events = {
            Qt.Key_0: lambda: self.key_num_clicked('0'),
            Qt.Key_1: lambda: self.key_num_clicked('1'),
            Qt.Key_2: lambda: self.key_num_clicked('2'),
            Qt.Key_3: lambda: self.key_num_clicked('3'),
            Qt.Key_4: lambda: self.key_num_clicked('4'),
            Qt.Key_5: lambda: self.key_num_clicked('5'),
            Qt.Key_6: lambda: self.key_num_clicked('6'),
            Qt.Key_7: lambda: self.key_num_clicked('7'),
            Qt.Key_8: lambda: self.key_num_clicked('8'),
            Qt.Key_9: lambda: self.key_num_clicked('9'),
            Qt.Key_Period: self.key_dot_Clicked,
            Qt.Key_Plus: lambda: self.key_oper_Clicked('+'),
            Qt.Key_Minus: lambda: self.key_oper_Clicked('-'),
            Qt.Key_Asterisk: lambda: self.key_oper_Clicked('*'),
            Qt.Key_Slash: lambda: self.key_oper_Clicked('/'),
            Qt.Key_Delete: self.key_clear_Clicked,
            Qt.Key_Backspace: self.key_bs_Clicked,
            Qt.Key_Enter: self.key_calc_Clicked,
            Qt.Key_Return: self.key_calc_Clicked,
        }

        if event.key() in events.keys():
            events[event.key()]()
    

    def setText(self, text):
        self.ui.output_field.setPlainText(text)
        self.calculate = text
        self.text = self.ui.output_field.toPlainText()
        self.ui.output_field.setAlignment(QtCore.Qt.AlignRight)

        

    def key_num_clicked(self, number):
        if self.text == 'Error!':
            self.setText(number)
        else:
            if number == 0:
                if self.text != str(0):
                    self.setText(self.text + number)
            else:
                if self.text != str(0):
                    self.setText(self.text + number)
                else:
                    self.setText(number)


    def key_dot_Clicked(self):
        if self.text == 'Error!':
            return    
        if '.' not in self.text or (self.text.count('.') == 1 and any(['+' in self.text, '-' in self.text, '/' in self.text, '*' in self.text])):
            self.setText(self.text + '.')


    def key_oper_Clicked(self, oper):
        if self.text == 'Error!':
            return
        if self.text[0] == '-' or not any(['+' in self.text, '-' in self.text, '/' in self.text, '*' in self.text]):
            self.setText(self.text + oper)
        elif self.text[0] == '-' or any(['+' == self.text[-1], '-' == self.text[-1], '/' == self.text[-1], '*' == self.text[-1]]):
            self.setText(self.text[:-1] + oper)


    def key_clear_Clicked(self):
        self.setText('0')


    def key_bs_Clicked(self):
        if self.text == 'Error!':
            self.key_clear_Clicked()
        if(len(self.text) == 1):
            self.setText('0')
        elif(self.text[-2] =='.'):
            self.setText(self.text[:-2])
        else:
            self.setText(self.text[:-1])


    def key_csign_Clicked(self):
        if self.text == 'Error!':
            return
        if self.text[0] == '-' or not any(['+' in self.text, '-' in self.text, '/' in self.text, '*' in self.text]):
            if self.text[0] == '-':
                self.setText(self.text[1:])
            else:
                self.setText('-' + self.text)


    def key_calc_Clicked(self):
        try:
            result = str(eval(self.calculate))
        except:
            self.setText("Error!")
            return
            
        if '.' in result and int(result.split('.')[1]) == 0:
            result = result.split('.')[0]

        self.setText(result)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
