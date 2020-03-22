# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Zoom_Notifier.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Zoom_Notifier(object):
    def setupUi(self, Zoom_Notifier):
        Zoom_Notifier.setObjectName("Zoom_Notifier")
        Zoom_Notifier.resize(388, 239)
        Zoom_Notifier.setIconSize(QtCore.QSize(25, 25))
        self.centralwidget = QtWidgets.QWidget(Zoom_Notifier)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(280, 20, 41, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.button1.setFont(font)
        self.button1.setAutoFillBackground(True)
        self.button1.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.button1.setObjectName("button1")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 20, 41, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.description = QtWidgets.QLineEdit(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(150, 20, 113, 21))
        self.description.setText("")
        self.description.setObjectName("description")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(20, 20, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        Zoom_Notifier.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Zoom_Notifier)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 388, 18))
        self.menubar.setObjectName("menubar")
        Zoom_Notifier.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Zoom_Notifier)
        self.statusbar.setObjectName("statusbar")
        Zoom_Notifier.setStatusBar(self.statusbar)

        self.retranslateUi(Zoom_Notifier)
        QtCore.QMetaObject.connectSlotsByName(Zoom_Notifier)

    def retranslateUi(self, Zoom_Notifier):
        _translate = QtCore.QCoreApplication.translate
        Zoom_Notifier.setWindowTitle(_translate("Zoom_Notifier", "Zoom_Notifier"))
        self.button1.setText(_translate("Zoom_Notifier", "Add"))
        self.pushButton.setText(_translate("Zoom_Notifier", "Del"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Zoom_Notifier = QtWidgets.QMainWindow()
    ui = Ui_Zoom_Notifier()
    ui.setupUi(Zoom_Notifier)
    Zoom_Notifier.show()
    sys.exit(app.exec_())
