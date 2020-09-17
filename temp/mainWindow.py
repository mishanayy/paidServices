# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(601, 560)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(601, 560))
        MainWindow.setMaximumSize(QSize(601, 560))
        self.menuExit = QAction(MainWindow)
        self.menuExit.setObjectName(u"menuExit")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.menuDogovor = QAction(MainWindow)
        self.menuDogovor.setObjectName(u"menuDogovor")
        self.menuDokuments = QAction(MainWindow)
        self.menuDokuments.setObjectName(u"menuDokuments")
        self.menuLoadUslugi = QAction(MainWindow)
        self.menuLoadUslugi.setObjectName(u"menuLoadUslugi")
        self.menuJournal = QAction(MainWindow)
        self.menuJournal.setObjectName(u"menuJournal")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 190, 581, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.printButton = QPushButton(self.horizontalLayoutWidget)
        self.printButton.setObjectName(u"printButton")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        self.printButton.setFont(font)
        self.printButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"res/printer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.printButton.setIcon(icon)
        self.printButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.printButton)

        self.clearButton = QPushButton(self.horizontalLayoutWidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u"res/document-new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearButton.setIcon(icon1)
        self.clearButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.clearButton)

        self.exitButton = QPushButton(self.horizontalLayoutWidget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u"res/system-exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitButton.setIcon(icon2)
        self.exitButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.exitButton)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 150, 581, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_NumDogovor = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_NumDogovor.setObjectName(u"lineEdit_NumDogovor")

        self.horizontalLayout.addWidget(self.lineEdit_NumDogovor)

        self.lineEdit_PriceUsluga = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_PriceUsluga.setObjectName(u"lineEdit_PriceUsluga")

        self.horizontalLayout.addWidget(self.lineEdit_PriceUsluga)

        self.lineEdit_NumReceipt = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_NumReceipt.setObjectName(u"lineEdit_NumReceipt")

        self.horizontalLayout.addWidget(self.lineEdit_NumReceipt)

        self.dateEdit = QDateEdit(self.horizontalLayoutWidget_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.dateEdit)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 581, 141))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_Fio = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_Fio.setObjectName(u"lineEdit_Fio")

        self.verticalLayout.addWidget(self.lineEdit_Fio)

        self.comboBox_Documents = QComboBox(self.verticalLayoutWidget)
        self.comboBox_Documents.setObjectName(u"comboBox_Documents")

        self.verticalLayout.addWidget(self.comboBox_Documents)

        self.lineEdit_NumDoc = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_NumDoc.setObjectName(u"lineEdit_NumDoc")

        self.verticalLayout.addWidget(self.lineEdit_NumDoc)

        self.lineEdit_Address = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_Address.setObjectName(u"lineEdit_Address")

        self.verticalLayout.addWidget(self.lineEdit_Address)

        self.comboBox_Usluga = QComboBox(self.verticalLayoutWidget)
        self.comboBox_Usluga.setObjectName(u"comboBox_Usluga")

        self.verticalLayout.addWidget(self.comboBox_Usluga)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QRect(10, 240, 581, 271))
        self.scrollArea.setFocusPolicy(Qt.NoFocus)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 579, 269))
        self.tableView = QTableView(self.scrollAreaWidgetContents)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 0, 581, 271))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 601, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_4 = QMenu(self.menu_2)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(8)
        self.statusbar.setFont(font1)
        self.statusbar.setStyleSheet(u"color: #474747;")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEdit_Fio, self.comboBox_Documents)
        QWidget.setTabOrder(self.comboBox_Documents, self.lineEdit_NumDoc)
        QWidget.setTabOrder(self.lineEdit_NumDoc, self.lineEdit_Address)
        QWidget.setTabOrder(self.lineEdit_Address, self.comboBox_Usluga)
        QWidget.setTabOrder(self.comboBox_Usluga, self.lineEdit_NumDogovor)
        QWidget.setTabOrder(self.lineEdit_NumDogovor, self.lineEdit_PriceUsluga)
        QWidget.setTabOrder(self.lineEdit_PriceUsluga, self.lineEdit_NumReceipt)
        QWidget.setTabOrder(self.lineEdit_NumReceipt, self.dateEdit)
        QWidget.setTabOrder(self.dateEdit, self.printButton)
        QWidget.setTabOrder(self.printButton, self.clearButton)
        QWidget.setTabOrder(self.clearButton, self.exitButton)
        QWidget.setTabOrder(self.exitButton, self.tableView)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menu.addAction(self.menuExit)
        self.menu_2.addAction(self.menuDogovor)
        self.menu_2.addAction(self.menu_4.menuAction())
        self.menu_2.addAction(self.menuDokuments)
        self.menu_4.addAction(self.menuLoadUslugi)
        self.menu_5.addAction(self.menuJournal)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0442\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.menuExit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.menuDogovor.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.menuDokuments.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.menuLoadUslugi.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0438", None))
        self.menuJournal.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b", None))
        self.printButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a\u0438", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u0443\u0433\u0438", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
    # retranslateUi

