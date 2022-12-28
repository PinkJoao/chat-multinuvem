# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'processWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ProcessWindow(object):
    def setupUi(self, ProcessWindow):
        if not ProcessWindow.objectName():
            ProcessWindow.setObjectName(u"ProcessWindow")
        ProcessWindow.resize(265, 248)
        self.centralwidget = QWidget(ProcessWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listMessages = QListWidget(self.centralwidget)
        self.listMessages.setObjectName(u"listMessages")

        self.verticalLayout.addWidget(self.listMessages)

        self.lineMessage = QLineEdit(self.centralwidget)
        self.lineMessage.setObjectName(u"lineMessage")

        self.verticalLayout.addWidget(self.lineMessage)

        ProcessWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProcessWindow)

        QMetaObject.connectSlotsByName(ProcessWindow)
    # setupUi

    def retranslateUi(self, ProcessWindow):
        ProcessWindow.setWindowTitle(QCoreApplication.translate("ProcessWindow", u"Mensagens", None))
        self.lineMessage.setPlaceholderText(QCoreApplication.translate("ProcessWindow", u"Nova mensagem", None))
    # retranslateUi

