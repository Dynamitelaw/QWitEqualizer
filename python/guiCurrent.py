# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qwitGui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from frequencyResponse import *
import bluetoothInterface as bt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 540)
        MainWindow.setStyleSheet("background-color: rgb(39, 40, 34);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.sliderA = QtWidgets.QSlider(self.centralwidget)
        self.sliderA.setMinimum(-56)
        self.sliderA.setMaximum(56)
        self.sliderA.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[0])))
        self.sliderA.setOrientation(QtCore.Qt.Vertical)
        self.sliderA.setObjectName("sliderA")
        self.verticalLayout.addWidget(self.sliderA, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.sliderB = QtWidgets.QSlider(self.centralwidget)
        self.sliderB.setMinimum(-56)
        self.sliderB.setMaximum(56)
        self.sliderB.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[1])))
        self.sliderB.setOrientation(QtCore.Qt.Vertical)
        self.sliderB.setObjectName("sliderB")
        self.verticalLayout_21.addWidget(self.sliderB, 0, QtCore.Qt.AlignHCenter)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_21.addWidget(self.label_21, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_21)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.sliderC = QtWidgets.QSlider(self.centralwidget)
        self.sliderC.setMinimum(-56)
        self.sliderC.setMaximum(56)
        self.sliderC.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[2])))
        self.sliderC.setOrientation(QtCore.Qt.Vertical)
        self.sliderC.setObjectName("sliderC")
        self.verticalLayout_23.addWidget(self.sliderC, 0, QtCore.Qt.AlignHCenter)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_23.addWidget(self.label_23, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_23)
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.sliderD = QtWidgets.QSlider(self.centralwidget)
        self.sliderD.setMinimum(-56)
        self.sliderD.setMaximum(56)
        self.sliderD.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[3])))
        self.sliderD.setOrientation(QtCore.Qt.Vertical)
        self.sliderD.setObjectName("sliderD")
        self.verticalLayout_31.addWidget(self.sliderD, 0, QtCore.Qt.AlignHCenter)
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_31.addWidget(self.label_31, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_31)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.sliderE = QtWidgets.QSlider(self.centralwidget)
        self.sliderE.setMinimum(-56)
        self.sliderE.setMaximum(56)
        self.sliderE.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[4])))
        self.sliderE.setOrientation(QtCore.Qt.Vertical)
        self.sliderE.setObjectName("sliderE")
        self.verticalLayout_22.addWidget(self.sliderE, 0, QtCore.Qt.AlignHCenter)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_22.addWidget(self.label_22, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_22)
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.sliderF = QtWidgets.QSlider(self.centralwidget)
        self.sliderF.setMinimum(-56)
        self.sliderF.setMaximum(56)
        self.sliderF.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[5])))
        self.sliderF.setOrientation(QtCore.Qt.Vertical)
        self.sliderF.setObjectName("sliderF")
        self.verticalLayout_33.addWidget(self.sliderF, 0, QtCore.Qt.AlignHCenter)
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_33.addWidget(self.label_33, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_33)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.sliderG = QtWidgets.QSlider(self.centralwidget)
        self.sliderG.setMinimum(-56)
        self.sliderG.setMaximum(56)
        self.sliderG.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[6])))
        self.sliderG.setOrientation(QtCore.Qt.Vertical)
        self.sliderG.setObjectName("sliderG")
        self.verticalLayout_24.addWidget(self.sliderG, 0, QtCore.Qt.AlignHCenter)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_24.addWidget(self.label_24, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_24)
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.sliderH = QtWidgets.QSlider(self.centralwidget)
        self.sliderH.setMinimum(-56)
        self.sliderH.setMaximum(56)
        self.sliderH.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[7])))
        self.sliderH.setOrientation(QtCore.Qt.Vertical)
        self.sliderH.setObjectName("sliderH")
        self.verticalLayout_30.addWidget(self.sliderH, 0, QtCore.Qt.AlignHCenter)
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_30.addWidget(self.label_30, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_30)
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.sliderI = QtWidgets.QSlider(self.centralwidget)
        self.sliderI.setMinimum(-56)
        self.sliderI.setMaximum(56)
        self.sliderI.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[8])))
        self.sliderI.setOrientation(QtCore.Qt.Vertical)
        self.sliderI.setObjectName("sliderI")
        self.verticalLayout_28.addWidget(self.sliderI, 0, QtCore.Qt.AlignHCenter)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_28.addWidget(self.label_28, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_28)
        self.verticalLayout_34 = QtWidgets.QVBoxLayout()
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.sliderJ = QtWidgets.QSlider(self.centralwidget)
        self.sliderJ.setMinimum(-56)
        self.sliderJ.setMaximum(56)
        self.sliderJ.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[9])))
        self.sliderJ.setOrientation(QtCore.Qt.Vertical)
        self.sliderJ.setObjectName("sliderJ")
        self.verticalLayout_34.addWidget(self.sliderJ, 0, QtCore.Qt.AlignHCenter)
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_34.addWidget(self.label_34, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_34)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.sliderK = QtWidgets.QSlider(self.centralwidget)
        self.sliderK.setMinimum(-56)
        self.sliderK.setMaximum(56)
        self.sliderK.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[10])))
        self.sliderK.setOrientation(QtCore.Qt.Vertical)
        self.sliderK.setObjectName("sliderK")
        self.verticalLayout_26.addWidget(self.sliderK, 0, QtCore.Qt.AlignHCenter)
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_26.addWidget(self.label_26, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_26)
        self.verticalLayout_36 = QtWidgets.QVBoxLayout()
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.sliderL = QtWidgets.QSlider(self.centralwidget)
        self.sliderL.setMinimum(-56)
        self.sliderL.setMaximum(56)
        self.sliderL.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[11])))
        self.sliderL.setOrientation(QtCore.Qt.Vertical)
        self.sliderL.setObjectName("sliderL")
        self.verticalLayout_36.addWidget(self.sliderL, 0, QtCore.Qt.AlignHCenter)
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_36.addWidget(self.label_36, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_36)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.sliderM = QtWidgets.QSlider(self.centralwidget)
        self.sliderM.setMinimum(-56)
        self.sliderM.setMaximum(56)
        self.sliderM.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[12])))
        self.sliderM.setOrientation(QtCore.Qt.Vertical)
        self.sliderM.setObjectName("sliderM")
        self.verticalLayout_25.addWidget(self.sliderM, 0, QtCore.Qt.AlignHCenter)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_25.addWidget(self.label_25, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_25)
        self.verticalLayout_35 = QtWidgets.QVBoxLayout()
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.sliderN = QtWidgets.QSlider(self.centralwidget)
        self.sliderN.setMinimum(-56)
        self.sliderN.setMaximum(56)
        self.sliderN.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[13])))
        self.sliderN.setOrientation(QtCore.Qt.Vertical)
        self.sliderN.setObjectName("sliderN")
        self.verticalLayout_35.addWidget(self.sliderN, 0, QtCore.Qt.AlignHCenter)
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_35.addWidget(self.label_35, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_35)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.sliderO = QtWidgets.QSlider(self.centralwidget)
        self.sliderO.setMinimum(-56)
        self.sliderO.setMaximum(56)
        self.sliderO.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[14])))
        self.sliderO.setOrientation(QtCore.Qt.Vertical)
        self.sliderO.setObjectName("sliderO")
        self.verticalLayout_27.addWidget(self.sliderO, 0, QtCore.Qt.AlignHCenter)
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_27.addWidget(self.label_27, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_27)
        self.verticalLayout_39 = QtWidgets.QVBoxLayout()
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.sliderP = QtWidgets.QSlider(self.centralwidget)
        self.sliderP.setMinimum(-56)
        self.sliderP.setMaximum(56)
        self.sliderP.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[15])))
        self.sliderP.setOrientation(QtCore.Qt.Vertical)
        self.sliderP.setObjectName("sliderP")
        self.verticalLayout_39.addWidget(self.sliderP, 0, QtCore.Qt.AlignHCenter)
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_39.addWidget(self.label_39, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_39)
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.sliderQ = QtWidgets.QSlider(self.centralwidget)
        self.sliderQ.setMinimum(-56)
        self.sliderQ.setMaximum(56)
        self.sliderQ.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[16])))
        self.sliderQ.setOrientation(QtCore.Qt.Vertical)
        self.sliderQ.setObjectName("sliderQ")
        self.verticalLayout_29.addWidget(self.sliderQ, 0, QtCore.Qt.AlignHCenter)
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_29.addWidget(self.label_29, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_29)
        self.verticalLayout_38 = QtWidgets.QVBoxLayout()
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.sliderR = QtWidgets.QSlider(self.centralwidget)
        self.sliderR.setMinimum(-56)
        self.sliderR.setMaximum(56)
        self.sliderR.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[17])))
        self.sliderR.setOrientation(QtCore.Qt.Vertical)
        self.sliderR.setObjectName("sliderR")
        self.verticalLayout_38.addWidget(self.sliderR, 0, QtCore.Qt.AlignHCenter)
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_38.addWidget(self.label_38, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_38)
        self.verticalLayout_37 = QtWidgets.QVBoxLayout()
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.sliderS = QtWidgets.QSlider(self.centralwidget)
        self.sliderS.setMinimum(-56)
        self.sliderS.setMaximum(56)
        self.sliderS.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[18])))
        self.sliderS.setOrientation(QtCore.Qt.Vertical)
        self.sliderS.setObjectName("sliderS")
        self.verticalLayout_37.addWidget(self.sliderS, 0, QtCore.Qt.AlignHCenter)
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_37.addWidget(self.label_37, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_37)
        self.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.sliderT = QtWidgets.QSlider(self.centralwidget)
        self.sliderT.setMinimum(-56)
        self.sliderT.setMaximum(56)
        self.sliderT.setSliderPosition(int(gainToDecibal(g_PreviousBandGains[19])))
        self.sliderT.setOrientation(QtCore.Qt.Vertical)
        self.sliderT.setObjectName("sliderT")
        self.verticalLayout_32.addWidget(self.sliderT, 0, QtCore.Qt.AlignHCenter)
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_32.addWidget(self.label_32, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_32)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Connect slider value changes to class method
        self.sliderA.sliderReleased.connect(self.gainChange)
        self.sliderB.sliderReleased.connect(self.gainChange)
        self.sliderC.sliderReleased.connect(self.gainChange)
        self.sliderD.sliderReleased.connect(self.gainChange)
        self.sliderE.sliderReleased.connect(self.gainChange)
        self.sliderF.sliderReleased.connect(self.gainChange)
        self.sliderG.sliderReleased.connect(self.gainChange)
        self.sliderH.sliderReleased.connect(self.gainChange)
        self.sliderI.sliderReleased.connect(self.gainChange)
        self.sliderJ.sliderReleased.connect(self.gainChange)
        self.sliderK.sliderReleased.connect(self.gainChange)
        self.sliderL.sliderReleased.connect(self.gainChange)
        self.sliderM.sliderReleased.connect(self.gainChange)
        self.sliderN.sliderReleased.connect(self.gainChange)
        self.sliderO.sliderReleased.connect(self.gainChange)
        self.sliderP.sliderReleased.connect(self.gainChange)
        self.sliderQ.sliderReleased.connect(self.gainChange)
        self.sliderR.sliderReleased.connect(self.gainChange)
        self.sliderS.sliderReleased.connect(self.gainChange)
        self.sliderT.sliderReleased.connect(self.gainChange)


    def gainChange(self):
        dBgains = [self.sliderA.value(), self.sliderB.value(), self.sliderC.value(), self.sliderD.value(), self.sliderE.value(), self.sliderF.value(), self.sliderG.value(), self.sliderH.value(), self.sliderI.value(), self.sliderJ.value(), self.sliderK.value(), self.sliderL.value(), self.sliderM.value(), self.sliderN.value(), self.sliderO.value(), self.sliderP.value(), self.sliderQ.value(), self.sliderR.value(), self.sliderS.value(), self.sliderT.value()]
        bandGains = [decibalToGain(g) for g in dBgains]
        bt.updateEqualizer(bandGains)

        responseData = findFrequencyResponse(bandGains)
        updateResponsePlot(responseData)
        while True:
            try:
                plt.pause(0.001)
                break
            except Exception as e:
                #print(e)
                pass
                

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">20 - 28.3 Hz</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">28.3 - 39.9 Hz</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">39.9 - 56.4 Hz</span></p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">56.4 - 79.6 Hz</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">79.6 - 113 Hz</span></p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">113 - 159 Hz</span></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">159 - 224 Hz</span></p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">224- 317 Hz</span></p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">317 - 448 Hz</span></p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">448 - 633 Hz</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">633 - 893 Hz</span></p></body></html>"))
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">893 Hz - 1.26 kHz</span></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">1.26 - 1.78 kHz</span></p></body></html>"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">1.78 - 2.52 kHz</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">2.52 - 3.56 kHz</span></p></body></html>"))
        self.label_39.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">3.56 - 5.02 kHz</span></p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">5.02 - 7.1 kHz</span></p></body></html>"))
        self.label_38.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">7.1 - 10 kHz</span></p></body></html>"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">10 - 14.2 kHz</span></p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#007ad9;\">14.2 - 20 kHz</span></p></body></html>"))


if __name__ == "__main__":
    #Reset equalizer to flat frequency response
    bt.resetEqualizerGains()

    #Restore gain information
    g_PreviousBandGains = bt.getGains()
    responseData = findFrequencyResponse(g_PreviousBandGains)
    updateResponsePlot(responseData)

    #Start gui
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

