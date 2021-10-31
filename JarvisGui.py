from datetime import time
from jarvisUi import Ui_JarvisUI
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from PyQt5.uic import loadUiType
import Main
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import webbrowser as web
import sys



class MainThread(QThread):

    def __init__(self):

        super(MainThread,self).__init__()

    def run(self):
        Main.Task_Gui()

startExe = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()

        self.gui = Ui_JarvisUI()
        self.gui.setupUi(self)
        self.gui.PushButton_start.clicked.connect(self.startTask)
       # self.gui.PushButton_start.clicked.connect(self.startMain)
        self.gui.PushButton_exit.clicked.connect(self.close)
        self.gui.PushButton_Chrome.clicked.connect(self.chrome_app)
        self.gui.PushButton_YouTube.clicked.connect(self.yt_app)
        self.gui.PushButton_VsCode.clicked.connect(self.VsCode_app)

    def chrome_app(self):
        Main.Speak("Opening Chrome")
        os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

    def yt_app(self):
        Main.Speak("Opening YouTube")
        web.open("https://www.youtube.com/")

    def VsCode_app(self):
        Main.Speak("Opening VS Code")
        os.startfile("C:\\Users\\valtt\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    def startTask(self):

        self.gui.label1 = QtGui.QMovie("C:\\JARVIS\\Material\\Iron_template.gif")
        self.gui.Gif_1.setMovie(self.gui.label1) #Change if needed
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("C:\\JARVIS\\Material\\jarvismk2.gif")
        self.gui.Gif_2.setMovie(self.gui.label2) #Change if needed
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("C:\\JARVIS\\Material\\VoiceReg.gif")
        self.gui.Gif_3.setMovie(self.gui.label3) #Change if needed
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("C:\\JARVIS\\Material\\voiceReg3.gif")
        self.gui.Gif_4.setMovie(self.gui.label4) #Change if needed
        self.gui.label4.start()

        startExe.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)
        startExe.start()

    
    def showTimeLive(self):
        t_ime = QTime.currentTime()
        time = t_ime.toString()
        d_ate = QDate.currentDate()
        date = d_ate.toString()
        label_time = "Time :"+ time
        label_date = "Date :"+ date

        self.gui.Text_time.setText(label_time)
        self.gui.Text_date.setText(label_date)


GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())