# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiMainWindow_OSX.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(246, 325)
        MainWindow.setMinimumSize(QtCore.QSize(246, 325))
        MainWindow.setMaximumSize(QtCore.QSize(246, 350))
        MainWindow.setInputMethodHints(QtCore.Qt.ImhDate|QtCore.Qt.ImhPreferUppercase)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 3, 221, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(4, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(5)
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 23))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setEnabled(True)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 3)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 7, 0, 1, 3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(80, 0))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setMaxLength(9)
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setDragEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(37, 16777215))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(3)
        self.lineEdit_2.setDragEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAcceptDrops(True)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setMaxLength(20)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setDragEnabled(True)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 9, 0, 1, 3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 4, 211, 221))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(4, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 6, 0, 1, 2)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_8.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setAcceptDrops(True)
        self.lineEdit_8.setText("")
        self.lineEdit_8.setMaxLength(20)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setDragEnabled(True)
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_3.addWidget(self.lineEdit_8, 7, 0, 1, 2)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_7.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setAcceptDrops(True)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setMaxLength(20)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setDragEnabled(True)
        self.lineEdit_7.setReadOnly(False)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_3.addWidget(self.lineEdit_7, 3, 0, 1, 2)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_3.addWidget(self.checkBox_2, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 2, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setEnabled(True)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 5, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 4, 0, 1, 2)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(80, 0))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setMaxLength(9)
        self.lineEdit_5.setFrame(True)
        self.lineEdit_5.setDragEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_3.addWidget(self.lineEdit_5, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_12.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 5, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 246, 22))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.action545 = QtWidgets.QAction(MainWindow)
        self.action545.setObjectName("action545")
        self.action54 = QtWidgets.QAction(MainWindow)
        self.action54.setObjectName("action54")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генератор"))
        self.pushButton.setText(_translate("MainWindow", "Сгенерировать"))
        self.label.setText(_translate("MainWindow", "BIC банка"))
        self.label_3.setText(_translate("MainWindow", "Валюта"))
        self.label_5.setText(_translate("MainWindow", "Группа    "))
        self.label_7.setText(_translate("MainWindow", "Сгенерированный счёт"))
        self.checkBox.setText(_translate("MainWindow", "Имеется корр. счёт"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Генерация счетов"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Генерация банковского счёта"))
        self.label_14.setText(_translate("MainWindow", "Сключёванный счёт"))
        self.checkBox_2.setText(_translate("MainWindow", "Корр. счёт"))
        self.label_10.setText(_translate("MainWindow", "BIC банка"))
        self.label_13.setText(_translate("MainWindow", "Счёт для ключевания"))
        self.label_11.setText(_translate("MainWindow", "Ключ"))
        self.pushButton_2.setText(_translate("MainWindow", "Сключевать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Ключевание"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Ключевание банковского счёта"))
        self.action545.setText(_translate("MainWindow", "545"))
        self.action54.setText(_translate("MainWindow", "54"))

