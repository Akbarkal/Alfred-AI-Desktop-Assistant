####---------------------------- Gui for Alfred ---------------------------------------

#### Created by: Mr. Akbar Kaleem

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('MainFiles\\Database\\alfred.ico'))
        MainWindow.setFixedSize(517,555)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(-150, -10, 811, 571))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("MainFiles\\Database\\icons\\gui.gif"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        self.Close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Close_btn.setGeometry(QtCore.QRect(170, 510, 181, 51))
        self.Close_btn.setStyleSheet("QPushButton{\n"
                                "color: skyblue;\n"
                                "font: 20pt \"Colonna MT\";\n"
                                "background-color: transparent;\n"
                                "border-radius : 10px;"
                                "}\n"
                                "QPushButton:hover{\n"
                                "    background-color: purple;\n"
                                "}")
        self.Close_btn.setObjectName("Close_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.Close_btn.hide()

        self.Start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Start_btn.setGeometry(QtCore.QRect(170, 510, 181, 51))
        self.Start_btn.setStyleSheet("QPushButton{\n"
                                "color: skyblue;\n"
                                "font: 20pt \"Colonna MT\";\n"
                                "background-color: transparent;\n"
                                "border-radius : 10px;"
                                "}\n"
                                "QPushButton:hover{\n"
                                "    background-color: purple;\n"
                                "}"
                                )
        self.Start_btn.setObjectName("Start_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.User_btn = QtWidgets.QPushButton(self.centralwidget)
        self.User_btn.setIcon(QtGui.QIcon("MainFiles\\Database\\icons\\user.png"))
        self.User_btn.setIconSize(QtCore.QSize(60,60))
        self.User_btn.setGeometry(QtCore.QRect(445, -5, 80, 70))
        self.User_btn.setStyleSheet("QPushButton{\n"
                                "color: purple;\n"
                                "font: 20pt \"Colonna MT\";\n"
                                "background-color: transparent;\n"
                                "border-radius : 10px;"
                                "}\n"
                                "\n"
                                "QPushButton:hover{\n"
                                "background-color: purple;\n"
                                "}")
        self.User_btn.setObjectName("User_btn")
        self.Contact_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Contact_btn.setIcon(QtGui.QIcon("MainFiles\\Database\\icons\\contact.png"))
        self.Contact_btn.setIconSize(QtCore.QSize(40,40))
        self.Contact_btn.setGeometry(QtCore.QRect(-10, -5, 80, 70))
        self.Contact_btn.setStyleSheet("QPushButton{\n"
                                "color: purple;\n"
                                "font: 20pt \"Colonna MT\";\n"
                                "background-color: transparent;\n"
                                "border-radius : 10px;"
                                "}\n"
                                "\n"
                                "QPushButton:hover{\n"
                                "background-color: purple;\n"
                                "}")
        
        self.Contact_btn.setObjectName("Contact_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Alfred A.I."))
        self.Start_btn.setText(_translate("MainWindow", "START"))
        self.Close_btn.setText(_translate("MainWindow", "SHUTDOWN"))
        self.User_btn.setText(_translate("MainWindow", ""))
        self.Contact_btn.setText(_translate("MainWindow", ""))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

####-------------------------------------- END ---------------------------------------