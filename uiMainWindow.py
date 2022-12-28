# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(543, 595)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.processLayout = QVBoxLayout()
        self.processLayout.setObjectName(u"processLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineNewProcess = QLineEdit(self.centralwidget)
        self.lineNewProcess.setObjectName(u"lineNewProcess")

        self.horizontalLayout_4.addWidget(self.lineNewProcess)

        self.buttonNewProcess = QPushButton(self.centralwidget)
        self.buttonNewProcess.setObjectName(u"buttonNewProcess")

        self.horizontalLayout_4.addWidget(self.buttonNewProcess)


        self.processLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.buttonDeleteProcess = QPushButton(self.centralwidget)
        self.buttonDeleteProcess.setObjectName(u"buttonDeleteProcess")

        self.horizontalLayout_7.addWidget(self.buttonDeleteProcess)

        self.buttonMigrateProcess = QPushButton(self.centralwidget)
        self.buttonMigrateProcess.setObjectName(u"buttonMigrateProcess")

        self.horizontalLayout_7.addWidget(self.buttonMigrateProcess)


        self.processLayout.addLayout(self.horizontalLayout_7)

        self.listProcess = QListWidget(self.centralwidget)
        self.listProcess.setObjectName(u"listProcess")

        self.processLayout.addWidget(self.listProcess)


        self.gridLayout_3.addLayout(self.processLayout, 1, 1, 1, 1)

        self.cloudLayout = QVBoxLayout()
        self.cloudLayout.setObjectName(u"cloudLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineNewCloud = QLineEdit(self.centralwidget)
        self.lineNewCloud.setObjectName(u"lineNewCloud")

        self.horizontalLayout.addWidget(self.lineNewCloud)

        self.buttonNewCloud = QPushButton(self.centralwidget)
        self.buttonNewCloud.setObjectName(u"buttonNewCloud")

        self.horizontalLayout.addWidget(self.buttonNewCloud)


        self.cloudLayout.addLayout(self.horizontalLayout)

        self.buttonDeleteCloud = QPushButton(self.centralwidget)
        self.buttonDeleteCloud.setObjectName(u"buttonDeleteCloud")

        self.cloudLayout.addWidget(self.buttonDeleteCloud)

        self.listClouds = QListWidget(self.centralwidget)
        self.listClouds.setObjectName(u"listClouds")

        self.cloudLayout.addWidget(self.listClouds)


        self.gridLayout_3.addLayout(self.cloudLayout, 0, 0, 1, 1)

        self.hostLayout = QVBoxLayout()
        self.hostLayout.setObjectName(u"hostLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineNewHost = QLineEdit(self.centralwidget)
        self.lineNewHost.setObjectName(u"lineNewHost")

        self.horizontalLayout_2.addWidget(self.lineNewHost)

        self.buttonNewHost = QPushButton(self.centralwidget)
        self.buttonNewHost.setObjectName(u"buttonNewHost")

        self.horizontalLayout_2.addWidget(self.buttonNewHost)


        self.hostLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.buttonDeleteHost = QPushButton(self.centralwidget)
        self.buttonDeleteHost.setObjectName(u"buttonDeleteHost")

        self.horizontalLayout_5.addWidget(self.buttonDeleteHost)

        self.buttonMigrateHost = QPushButton(self.centralwidget)
        self.buttonMigrateHost.setObjectName(u"buttonMigrateHost")

        self.horizontalLayout_5.addWidget(self.buttonMigrateHost)


        self.hostLayout.addLayout(self.horizontalLayout_5)

        self.listHosts = QListWidget(self.centralwidget)
        self.listHosts.setObjectName(u"listHosts")

        self.hostLayout.addWidget(self.listHosts)


        self.gridLayout_3.addLayout(self.hostLayout, 0, 1, 1, 1)

        self.vmLayout = QVBoxLayout()
        self.vmLayout.setObjectName(u"vmLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineNewVM = QLineEdit(self.centralwidget)
        self.lineNewVM.setObjectName(u"lineNewVM")

        self.horizontalLayout_3.addWidget(self.lineNewVM)

        self.buttonNewVM = QPushButton(self.centralwidget)
        self.buttonNewVM.setObjectName(u"buttonNewVM")

        self.horizontalLayout_3.addWidget(self.buttonNewVM)


        self.vmLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.buttonDeleteVM = QPushButton(self.centralwidget)
        self.buttonDeleteVM.setObjectName(u"buttonDeleteVM")

        self.horizontalLayout_6.addWidget(self.buttonDeleteVM)

        self.buttonMigrateVM = QPushButton(self.centralwidget)
        self.buttonMigrateVM.setObjectName(u"buttonMigrateVM")

        self.horizontalLayout_6.addWidget(self.buttonMigrateVM)


        self.vmLayout.addLayout(self.horizontalLayout_6)

        self.listVMs = QListWidget(self.centralwidget)
        self.listVMs.setObjectName(u"listVMs")

        self.vmLayout.addWidget(self.listVMs)


        self.gridLayout_3.addLayout(self.vmLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Multinuvens", None))
        self.lineNewProcess.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do Processo", None))
        self.buttonNewProcess.setText(QCoreApplication.translate("MainWindow", u"Criar Processo", None))
        self.buttonDeleteProcess.setText(QCoreApplication.translate("MainWindow", u"Excluir Processo", None))
        self.buttonMigrateProcess.setText(QCoreApplication.translate("MainWindow", u"Migrar Processo", None))
        self.lineNewCloud.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome da Nuvem", None))
        self.buttonNewCloud.setText(QCoreApplication.translate("MainWindow", u"Criar Nuvem", None))
        self.buttonDeleteCloud.setText(QCoreApplication.translate("MainWindow", u"Excluir Nuvem", None))
        self.lineNewHost.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do Host", None))
        self.buttonNewHost.setText(QCoreApplication.translate("MainWindow", u"Criar Host", None))
        self.buttonDeleteHost.setText(QCoreApplication.translate("MainWindow", u"Excluir Host", None))
        self.buttonMigrateHost.setText(QCoreApplication.translate("MainWindow", u"Migrar Host", None))
        self.lineNewVM.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome da VM", None))
        self.buttonNewVM.setText(QCoreApplication.translate("MainWindow", u"Criar VM", None))
        self.buttonDeleteVM.setText(QCoreApplication.translate("MainWindow", u"Excluir VM", None))
        self.buttonMigrateVM.setText(QCoreApplication.translate("MainWindow", u"Migrar VM", None))
    # retranslateUi

