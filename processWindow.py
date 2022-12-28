# PYSIDE6 IMPORTS ___________________________________________________________________________________________________
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from uiProcessWindow import Ui_ProcessWindow
from PySide6.QtCore import QTimer

# APP CLASS _________________________________________________________________________________________________________
class ProcessWindow(QMainWindow, Ui_ProcessWindow):
    def __init__(self, motherWindow, process):
        super(ProcessWindow, self).__init__()
        self.setupUi(self)

        self.motherWindow = motherWindow
        self.process = process[0]
        self.process.window = self

        self.setWindowTitle('Mensagens - ' + self.process.name)

        self.listMessages.addItems(self.process.messages)

        self.lineMessage.returnPressed.connect(lambda: self.sendMessage(self.lineMessage.text()))

    def updateMessages(self):
        self.listMessages.clear()
        self.listMessages.addItems(self.process.messages)

    def sendMessage(self, text):
        self.lineMessage.clear()
        self.process.sendMessage(text)

# CLOSE APP EVENT ___________________________________________________________________________________________________
    def closeEvent(self, event):
        can_exit = True

        self.motherWindow.processWindows.remove(self)

        if can_exit:
            event.accept()
        else:
            event.ignore()

