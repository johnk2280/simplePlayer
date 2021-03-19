# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import QVideoWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1319, 627)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.video_layout = QtWidgets.QHBoxLayout()
        self.video_layout.setObjectName("video_layout")
        self.video_widget_left = QVideoWidget(self.centralwidget)
        self.video_widget_left.setMinimumSize(QtCore.QSize(640, 480))
        self.video_widget_left.setObjectName("video_widget_left")
        self.video_layout.addWidget(self.video_widget_left)
        self.video_widget_right = QVideoWidget(self.centralwidget)
        self.video_widget_right.setMinimumSize(QtCore.QSize(640, 480))
        self.video_widget_right.setObjectName("video_widget_right")
        self.video_layout.addWidget(self.video_widget_right)
        self.verticalLayout.addLayout(self.video_layout)

        self.slider_layout = QtWidgets.QHBoxLayout()
        self.slider_layout.setObjectName("slider_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.slider_layout.addItem(spacerItem)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(640, 0))
        self.horizontalSlider.setMaximumSize(QtCore.QSize(960, 16777215))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.slider_layout.addWidget(self.horizontalSlider)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.slider_layout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.slider_layout)

        self.control_layout = QtWidgets.QHBoxLayout()
        self.control_layout.setObjectName("control_layout")
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setObjectName("open_button")
        self.control_layout.addWidget(self.open_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.control_layout.addItem(spacerItem2)
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setObjectName("stop_button")
        self.control_layout.addWidget(self.stop_button)
        self.prev_button = QtWidgets.QPushButton(self.centralwidget)
        self.prev_button.setObjectName("prev_button")
        self.control_layout.addWidget(self.prev_button)
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setObjectName("play_button")
        self.control_layout.addWidget(self.play_button)
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setObjectName("next_button")
        self.control_layout.addWidget(self.next_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.control_layout.addItem(spacerItem3)
        self.quit_button = QtWidgets.QPushButton(self.centralwidget)
        self.quit_button.setObjectName("quit_button")
        self.control_layout.addWidget(self.quit_button)
        self.verticalLayout.addLayout(self.control_layout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1319, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.action_quit = QtWidgets.QAction(MainWindow)
        self.action_quit.setObjectName("action_quit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ONI_viewer"))
        self.open_button.setText(_translate("MainWindow", "Open"))
        self.stop_button.setText(_translate("MainWindow", 'Stop'))
        self.prev_button.setText(_translate("MainWindow", "Previous"))
        self.play_button.setText(_translate("MainWindow", "Play"))
        self.next_button.setText(_translate("MainWindow", "Next"))
        self.quit_button.setText(_translate("MainWindow", "Quit"))
        self.action_open.setText(_translate("MainWindow", "Open"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.action_quit.setText(_translate("MainWindow", "Quit"))


