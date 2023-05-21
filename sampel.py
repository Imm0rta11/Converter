from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(587, 233)
        MainWindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.157635 rgba(0, 112, 112, 255), stop:1 rgba(255, 255, 255, 255))\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 281, 71))
        self.pushButton.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0))")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 150, 411, 41))
        self.label.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0))")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 170, 113, 32))
        self.pushButton_2.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 10, 271, 71))
        self.pushButton_3.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0))")
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(450, 90, 111, 26))
        self.comboBox.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0))")
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p>body{</p><p>background-color:#4e1764</p><p>}</p></body></html>"))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>body{</p><p>background-color:#4e1764</p><p>}</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Select File MP4"))
        self.label.setText(_translate("MainWindow", 'Derectory'))
        self.pushButton_2.setText(_translate("MainWindow", "Convert"))
        self.pushButton_3.setText(_translate("MainWindow", "Select File MP3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
