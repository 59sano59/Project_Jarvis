from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JarvisUI(object):
    def setupUi(self, JarvisUI):
        JarvisUI.setObjectName("JarvisUI")
        JarvisUI.resize(1624, 899) #change if needed
        self.centralwidget = QtWidgets.QWidget(JarvisUI)
        self.centralwidget.setObjectName("centaralwidget")
        self.bg_1 = QtWidgets.QLabel(self.centralwidget)
        self.bg_1.setGeometry(QtCore.QRect(0, 0, 1621, 861))
        self.bg_1.setText("")
        self.bg_1.setPixmap(QtGui.QPixmap("C:\\JARVIS\\Material\\black_template2.jpg"))#get Black_Template pic 
        self.bg_1.setScaledContents(True)
        self.bg_1.setObjectName("bg_1")

        self.bg_2 = QtWidgets.QLabel(self.centralwidget)
        self.bg_2.setGeometry(QtCore.QRect(530, 10, 541, 331))
        self.bg_2.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"background-color: rgb(0, 255, 255);")
        self.bg_2.setText("")
        self.bg_2.setObjectName("bg_2")

        #self.bg_3 = QtWidgets.QLabel(self.centralwidget)
        #self.bg_3.setGeometry(QtCore.QRect(20, 20, 591, 361))
        #self.bg_3.setStyleSheet("background-color: rgb(0, 255, 255);\n"
#"background-color: rgb(16, 178, 214);")
 #       self.bg_3.setText("")
  #      self.bg_3.setObjectName("bg_3")

        self.bg_4 = QtWidgets.QLabel(self.centralwidget)
        self.bg_4.setGeometry(QtCore.QRect(1230, 40, 361, 251))
        self.bg_4.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"background-color: rgb(0, 255, 255);")
        self.bg_4.setText("")
        self.bg_4.setObjectName("bg_4")

        self.bg_5 = QtWidgets.QLabel(self.centralwidget)
        self.bg_5.setGeometry(QtCore.QRect(1230, 310, 361, 131))
        self.bg_5.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"background-color: rgb(0, 255, 255);")
        self.bg_5.setText("")
        self.bg_5.setObjectName("bg_5")

        #use when needed
        #self.bg_6 = QtWidgets.QLabel(self.centralwidget)
        #self.bg_6.setGeometry(QtCore.Qrect(1090, 540, 271, 71))
        #self.bg_6.setText("")
        #self.bg_6.setPixmap("")#path for text pick
        #self.bg_6.setScaledContents(True)
        #self.bg_6.setObjectName("bg_6")

        self.Gif_1 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_1.setGeometry(QtCore.QRect(20, 20, 481, 311))
        self.Gif_1.setText("")
        self.Gif_1.setPixmap(QtGui.QPixmap("C:\\JARVIS\\Material\\Iron_template.gif"))
        self.Gif_1.setScaledContents(True)
        self.Gif_1.setObjectName("Gif_1")

        self.Gif_2 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_2.setGeometry(QtCore.QRect(540, 20, 521, 311))
        self.Gif_2.setText("")
        self.Gif_2.setPixmap(QtGui.QPixmap("C:\\JARVIS\\Material\\jarvismk2.gif"))
        self.Gif_2.setScaledContents(True)
        self.Gif_2.setObjectName("Gif_2")

        self.Gif_3 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_3.setGeometry(QtCore.QRect(50, 470, 551, 321))
        self.Gif_3.setText("")
        self.Gif_3.setPixmap(QtGui.QPixmap("C:\\JARVIS\\Material\\VoiceReg.gif"))
        self.Gif_3.setScaledContents(True)
        self.Gif_3.setObjectName("Gif_3")

        self.Gif_4 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_4.setGeometry(QtCore.QRect(1250, 60, 321, 211))
        self.Gif_4.setText("")
        self.Gif_4.setPixmap(QtGui.QPixmap("C:\\JARVIS\\Material\\voiceReg3.gif"))
        self.Gif_4.setScaledContents(True)
        self.Gif_4.setObjectName("Gif_4")

        #optional gif take away if it doesn't fit well
        #self.Gif_5 = QtWidgets.QLabel(self.centralwidget)
        #self.Gif_5.setGeometry(QtCore.QRect(1110, 690, 441, 151))
        #self.Gif_5.setText("")
        #self.Gif_5.setPixmap(QtGui.QPixmap("C:\\JARVIS\\Material\\initial.gif"))
        #self.Gif_5.setScaledContents(True)
        #self.Gif_5.setObjectName("Gif_5")

        self.Text_time = QtWidgets.QTextBrowser(self.centralwidget)
        self.Text_time.setGeometry(QtCore.QRect(1250, 750, 271, 71))
        self.Text_time.setStyleSheet("background-color: Transparent;\n"
"font: 18pt MS Shell Dlg 2;\n"
"border-radious:none;\n"
"color: rgb(0, 255, 255);")
        self.Text_time.setObjectName("Text_time")

        self.Text_date = QtWidgets.QTextBrowser(self.centralwidget)
        self.Text_date.setGeometry(QtCore.QRect(1250, 650, 271, 71))
        self.Text_date.setStyleSheet("background-color: Transparent;\n"
"font: 18pt MS Shell Dlg 2;\n"
"border-radious:none;\n"
"color: rgb(0, 255, 255);")
        self.Text_date.setObjectName("Text_date")

      #  self.Text_day = QtWidgets.QTextBrowser(self.centralwidget)
       # self.Text_day.setGeometry(QtCore.QRect(1250, 550, 271, 71))
        #self.Text_day.setStyleSheet("background-color: Transparent;\n"
#"border-radious:none;\n"
#"color: rgb(0, 255, 255);")
 #       self.Text_day.setObjectName("Text_day")

        self.PushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_start.setGeometry(QtCore.QRect(1250, 320, 321, 51))
        self.PushButton_start.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 18pt MS Shell Dlg 2;\n"
"color: rgb(0, 255, 255);\n"
"\n"
"")
        self.PushButton_start.setObjectName("PushButton_start")

        self.PushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_exit.setGeometry(QtCore.QRect(1250, 380, 321, 51))
        self.PushButton_exit.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 18pt MS Shell Dlg 2;\n"
"color: rgb(0, 255, 255);\n"
"\n"
"")
        self.PushButton_start.setObjectName("PushButton_exit")

      #  self.Text_Temperture = QtWidgets.QTextBrowser(self.centralwidget)
       # self.Text_Temperture.setGeometry(QtCore.QRect(1250, 450, 271, 71))
       # self.Text_Temperture.setStyleSheet("background-color: Transparent;\n"
#"border-radious:none;\n"
#"color: rgb(0, 255, 255);")

        self.PushButton_Chrome = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_Chrome.setGeometry(QtCore.QRect(840, 410, 181, 61))
        self.PushButton_Chrome.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 18pt MS Shell Dlg 2;\n"
"\n"
"")
        self.PushButton_Chrome.setObjectName("PushButton_Chrome")       

        self.PushButton_YouTube = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_YouTube.setGeometry(QtCore.QRect(650, 410, 181, 61))
        self.PushButton_YouTube.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 18pt MS Shell Dlg 2;\n"
"\n"
"")
        self.PushButton_Chrome.setObjectName("PushButton_YouTube")  

        self.PushButton_VsCode = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_VsCode.setGeometry(QtCore.QRect(1030, 410, 181, 61))
        self.PushButton_VsCode.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 18pt MS Shell Dlg 2;\n"
"\n"
"")
        self.PushButton_Chrome.setObjectName("PushButton_VsCode")  

        self.Gif_1.raise_()
        self.Gif_2.raise_()
        self.Gif_3.raise_()
        self.Gif_4.raise_()
        self.PushButton_exit.raise_()
        self.PushButton_start.raise_()
        self.PushButton_YouTube.raise_()
        self.PushButton_Chrome.raise_()
        self.PushButton_VsCode.raise_()
        JarvisUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(JarvisUI)
        QtCore.QMetaObject.connectSlotsByName(JarvisUI)

    def retranslateUi(self, JarvisUI):
        _translate = QtCore.QCoreApplication.translate
        JarvisUI.setWindowTitle(_translate("JarvisUI", "MainWindow"))
        self.PushButton_start.setText(_translate("JarvisUI", "START"))
        self.PushButton_exit.setText(_translate("JarvisUI", "EXIT"))
        self.PushButton_YouTube.setText(_translate("JarvisUI", "YouTube"))
        self.PushButton_Chrome.setText(_translate("JarvisUI", "Chrome"))
        self.PushButton_VsCode.setText(_translate("JarvisUI", "VsCode"))


if __name__== "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JarvisUI = QtWidgets.QMainWindow()
    ui = Ui_JarvisUI()
    ui.setupUi(JarvisUI)
    JarvisUI.show()
    sys.exit(app.exec_())
    