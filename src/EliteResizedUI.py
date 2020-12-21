# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConverterGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
import Settings


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(100, 510, 691, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 520, 71, 16))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 290, 761, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(230, 10, 551, 261))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(450, 30, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 301, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 110, 301, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 110, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 190, 301, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 190, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 190, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 240, 201, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 120, 201, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.radioButton_1_png = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_1_png.setGeometry(QtCore.QRect(170, 10, 16, 17))
        self.radioButton_1_png.setText("")
        self.radioButton_1_png.setObjectName("radioButton_1_png")
        self.radioButton_1_png.setChecked(True)
        self.radioButton_2_jpeg = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_2_jpeg.setGeometry(QtCore.QRect(170, 40, 16, 17))
        self.radioButton_2_jpeg.setText("")
        self.radioButton_2_jpeg.setObjectName("radioButton_2_jpeg")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(20, 40, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.radioButton_3_webp = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_3_webp.setGeometry(QtCore.QRect(170, 70, 16, 17))
        self.radioButton_3_webp.setText("")
        self.radioButton_3_webp.setObjectName("radioButton_3_webp")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(20, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(lambda: self.browseSlot("journal"))
        self.pushButton_2.clicked.connect(lambda: self.browseSlot("screenshots"))
        self.pushButton_3.clicked.connect(lambda: self.browseSlot("save"))
        self.pushButton_4.clicked.connect(self.convert)
        self.lineEdit.returnPressed.connect(lambda: self.returnPressedSlot("journal"))
        self.lineEdit_2.returnPressed.connect(lambda: self.returnPressedSlot("screenshots"))
        self.lineEdit_3.returnPressed.connect(lambda: self.returnPressedSlot("save"))
        self.radioButton_1_png.toggled.connect(lambda: self.onClicked("png"))
        self.radioButton_2_jpeg.toggled.connect(lambda: self.onClicked("jpeg"))
        self.radioButton_3_webp.toggled.connect(lambda: self.onClicked("webp"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Elite Resized (Ver 0.1.0 Alpha)"))
        self.label.setText(_translate("MainWindow", "% Converted"))
        self.label_2.setText(_translate("MainWindow", "Elite Resized"))
        self.label_3.setText(_translate("MainWindow", "Elite Dangerous Screenshot Shrinker by BeardOfRice"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.label_4.setText(_translate("MainWindow", "Journal location"))
        self.label_5.setText(_translate("MainWindow", "Screenshots location"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.label_6.setText(_translate("MainWindow", "Save location"))
        self.pushButton_3.setText(_translate("MainWindow", "Browse"))
        self.pushButton_4.setText(_translate("MainWindow", "Convert"))
        self.label_7.setText(_translate("MainWindow", "png"))
        self.label_8.setText(_translate("MainWindow", "jpeg"))
        self.label_9.setText(_translate("MainWindow", "webp"))
        self.lineEdit.setText(self.journalDir)
        self.lineEdit_2.setText(self.screenshotDir)
        self.lineEdit_3.setText(self.saveDir)
        self.progressBar.setValue(Settings.completed)

    @pyqtSlot( )
    def returnPressedSlot( self ):
        pass

    @pyqtSlot( )
    def browseSlot( self ):
        pass

    @pyqtSlot( )
    def convert( self ):
        pass

    @pyqtSlot()
    def onClicked( self ):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())