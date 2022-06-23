
# Form implementation generated from reading ui file 'form.ui'



from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep


class Ui_Form(object):
        # setup UI
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(704, 506)
        Form.setStyleSheet("QWidget{\n"
"    background: black\n"
"}")


        # founction part


                ##### function for set counter
        def setting_label():
                m = self.spinBox.value()
                h = self.spinBox_2.value()
                s = self.spinBox_3.value()
                global t
                t = h * 3600
                t = t + (m*60)
                t = t + s
                timer = "{:02d}:{:02d}:{:02d}".format(h,m,s)
                self.label.setText(timer)
        
        def pause(y=False):
                global pause
                if y == True: 
                        pause = True
                        return pause
                else: 
                        pause = False
                        return pause   

                ##### function for start countdown
        def start_countDown(t):
                while t:
                        h  = t // 3600
                        m  = t // 60
                        s  = t % 60
                        timer = "{:02d}:{:02d}:{:02d}".format(h,m,s)
                        self.label.setText(timer)
                        app.processEvents()
                        sleep(1)
                        if pause==True:
                                t-=0
                        else:
                                t-=1
                self.label.setText("00:00:00")        

                        







        self.pushButton = QtWidgets.QPushButton(Form, clicked = lambda : setting_label())
        self.pushButton.setGeometry(QtCore.QRect(380, 46, 112, 34))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background:black;\n"
"    color:#fff;\n"
"    border: 1px solid #fff\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form ,clicked = lambda : start_countDown(t))
        self.pushButton_2.clicked.connect(lambda: pause())
        self.pushButton_2.setGeometry(QtCore.QRect(240, 90, 112, 34))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background:black;\n"
"    color:#fff;\n"
"    border: 1px solid #fff\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form,clicked = lambda : pause(True))
        self.pushButton_3.setGeometry(QtCore.QRect(360, 90, 112, 34))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background:black;\n"
"    color:#fff;\n"
"    border: 1px solid #fff\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 240, 401, 91))
        self.label.setStyleSheet("QLabel{\n"
"font-size:100px;\n"
"text-align:center;\n"
"    color:#fff;\n"
"\n"
"}")
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(270, 50, 45, 25))
        self.spinBox.setStyleSheet("QSpinBox{\n"
"    background:black;\n"
"    color:#fff;\n"
"    border: 1px solid #fff\n"
"}")
        self.spinBox.setMaximum(60)
        self.spinBox.setObjectName("spinBox")





        self.spinBox_2 = QtWidgets.QSpinBox(Form)
        self.spinBox_2.setGeometry(QtCore.QRect(220, 50, 45, 25))
        self.spinBox_2.setStyleSheet("QSpinBox{\n"
"    background:black;\n"
"    color:#fff;\n"
"    border: 1px solid #fff\n"
"}")
        self.spinBox_2.setMaximum(24)
        self.spinBox_2.setObjectName("spinBox_2")





        self.spinBox_3 = QtWidgets.QSpinBox(Form)
        self.spinBox_3.setGeometry(QtCore.QRect(320, 50, 45, 25))
        self.spinBox_3.setStyleSheet("QSpinBox{\n"
"    background:black;\n"
"    color:#fff;\n"
"    border: 1px solid #fff\n"
"}")
        self.spinBox_3.setMaximum(60)
        self.spinBox_3.setObjectName("spinBox_3")






        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Set"))
        self.pushButton_2.setText(_translate("Form", "Start"))
        self.pushButton_3.setText(_translate("Form", "Pause"))
        self.label.setText(_translate("Form", "00:00:00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
