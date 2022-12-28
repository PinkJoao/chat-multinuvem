# PYSIDE6 IMPORTS ___________________________________________________________________________________________________
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from uiMainWindow import Ui_MainWindow
from processWindow import ProcessWindow

# APP IMPORTS _______________________________________________________________________________________________________
from threading import Thread
from multinuvem import MultiCloud
import os

# GLOBALS ___________________________________________________________________________________________________________
APP = ''
multiCloud = MultiCloud()


# APP CLASS _________________________________________________________________________________________________________
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.buttonNewCloud.clicked.connect(lambda: newCloud(self.lineNewCloud.text()))
        self.buttonNewHost.clicked.connect(lambda: newHost(self.lineNewHost.text(), self.listClouds.currentItem().text(), self.buttonNewHost.text()))
        self.buttonNewVM.clicked.connect(lambda: newVM(self.lineNewVM.text(), self.listHosts.currentItem().text(), self.buttonNewVM.text()))
        self.buttonNewProcess.clicked.connect(lambda: newProcess(self.lineNewProcess.text(), self.listVMs.currentItem().text(), self.buttonNewProcess.text()))

        self.buttonDeleteCloud.clicked.connect(lambda: deleteCloud(self.listClouds.currentItem().text()))
        self.buttonDeleteHost.clicked.connect(lambda: deleteHost(self.listHosts.currentItem().text()))
        self.buttonDeleteVM.clicked.connect(lambda: deleteVM(self.listVMs.currentItem().text()))
        self.buttonDeleteProcess.clicked.connect(lambda: deleteProcess(self.listProcess.currentItem().text()))

        self.buttonMigrateHost.clicked.connect(lambda: migrateHost(self.listHosts.currentItem().text(), self.listClouds.currentItem().text(), self.listHosts.currentRow()))
        self.buttonMigrateVM.clicked.connect(lambda: migrateVM(self.listVMs.currentItem().text(), self.listHosts.currentItem().text(), self.listVMs.currentRow(), True))
        self.buttonMigrateProcess.clicked.connect(lambda: migrateProcess(self.listProcess.currentItem().text(), self.listVMs.currentItem().text(), self.listProcess.currentRow(), True))

        self.listHosts.itemClicked.connect(lambda: self.buttonNewHost.setText('Renomear'))
        self.listHosts.itemSelectionChanged.connect(lambda: self.buttonNewHost.setText('Criar Host'))

        self.listVMs.itemClicked.connect(lambda: self.buttonNewVM.setText('Renomear'))
        self.listVMs.itemSelectionChanged.connect(lambda: self.buttonNewVM.setText('Criar VM'))

        self.listProcess.itemClicked.connect(lambda: self.buttonNewProcess.setText('Renomear'))
        self.listProcess.itemSelectionChanged.connect(lambda: self.buttonNewProcess.setText('Criar Processo'))

        self.listProcess.itemDoubleClicked.connect(lambda: self.openProcess(self.listProcess.currentItem().text()))

        self.processWindows = []


# APP METHODS _______________________________________________________________________________________________________


    def openProcess(self, process):
        cloud, host, vm, process = process.split(' - ')
        process = multiCloud.searchProcess(process, vm, host, cloud)
        self.processWindows.append(ProcessWindow(self, process))
        window = len(self.processWindows) - 1
        self.processWindows[window].show()


# CLOSE APP EVENT ___________________________________________________________________________________________________


    def closeEvent(self, event):
        can_exit = True

        close()
        os.system('taskkill /f /im main.exe')

        if can_exit:
            event.accept()
        else:
            event.ignore()

# PUBLIC METHODS ____________________________________________________________________________________________________


def close():
    for row in range(APP.listProcess.count()):
        cloud, host, vm, process = APP.listProcess.item(row).text().split(' - ')
        multiCloud.deleteProcess(process, vm, host, cloud)


def newCloud(newCloudName):
    if newCloudName != '':
        APP.lineNewCloud.setText('')
        if multiCloud.addNewCloud(newCloudName):
            APP.listClouds.addItem(newCloudName)
            APP.lineNewCloud.setPlaceholderText('Nome da Nuvem')
        else:
            APP.lineNewCloud.setPlaceholderText('Nome indisponível')


def newHost(newHostName, father, button):
    if newHostName != '':
        APP.lineNewHost.setText('')
        if button == 'Criar Host':
            if multiCloud.addNewHost(newHostName, father):
                APP.listHosts.addItem(father + ' - ' + newHostName)
                APP.lineNewHost.setPlaceholderText('Nome do Host')
                return True
            else:
                APP.lineNewHost.setPlaceholderText('Nome indisponível')
        else:
            renameHost(APP.listHosts.currentRow(), newHostName)


def newVM(newVMName, family, button):
    if newVMName != '':
        APP.lineNewVM.setText('')
        if button == 'Criar VM':
            cloud, host = family.split(' - ')
            if multiCloud.addNewVM(newVMName, host, cloud):
                APP.listVMs.addItem(family + ' - ' + newVMName)
                APP.lineNewVM.setPlaceholderText('Nome da VM')
                return True
            else:
                APP.lineNewVM.setPlaceholderText('Nome indisponível')
        else:
            renameVM(APP.listVMs.currentRow(), newVMName)


def newProcess(newProcessName, family, button):
    if newProcessName != '':
        APP.lineNewProcess.setText('')
        if button == 'Criar Processo':
            cloud, host, vm = family.split(' - ')
            if multiCloud.addNewProcess(newProcessName, vm, host, cloud):
                APP.listProcess.addItem(family + ' - ' + newProcessName)
                APP.lineNewProcess.setPlaceholderText('Nome do Processo')
                return True
            else:
                APP.lineNewProcess.setPlaceholderText('Nome indisponível')
        else:
            renameProcess(APP.listProcess.currentRow(), newProcessName)


def renameHost(itemRow, newName):
    cloud, host = APP.listHosts.item(itemRow).text().split(' - ')

    if newHost(newName, cloud, 'Criar Host'):
        for row in range(APP.listVMs.count()):
            rowCloud, rowHost, rowVM = APP.listVMs.item(row).text().split(' - ')
            if rowCloud == cloud and rowHost == host:
                family = APP.listVMs.item(row).text()
                newFather = cloud + ' - ' + newName
                migrateVM(family, newFather, row, True)

        deleteHost(APP.listHosts.item(itemRow).text())


def renameVM(itemRow, newName):
    cloud, host, vm = APP.listVMs.item(itemRow).text().split(' - ')
    oldFamily = cloud + ' - ' + host
    if newVM(newName, oldFamily, 'Criar VM'):
        for row in range(APP.listProcess.count()):
            rowCloud, rowHost, rowVM, rowProcess = APP.listProcess.item(row).text().split(' - ')
            if rowCloud == cloud and rowHost == host and rowVM == vm:
                family = APP.listProcess.item(row).text()
                newFather = cloud + ' - ' + host + ' - ' + newName
                migrateProcess(family, newFather, row, True)

        deleteVM(APP.listVMs.item(itemRow).text())


def renameProcess(itemRow, newName):
    cloud, host, vm, process = APP.listProcess.item(itemRow).text().split(' - ')
    oldFamily = cloud + ' - ' + host + ' - ' + vm

    object = multiCloud.searchProcess(process, vm, host, cloud)
    object[0].name = newName
    newObject = (object[0], newName)
    object[0].father.process.remove(object)
    object[0].father.process.append(newObject)
    APP.listProcess.takeItem(itemRow)
    APP.listProcess.addItem(oldFamily + ' - ' + newName)


def deleteCloud(cloud):
    if multiCloud.deleteCloud(cloud):
        item = APP.listClouds.currentRow()
        item = APP.listClouds.takeItem(item)
        del item
    else:
        APP.lineNewCloud.setPlaceholderText('A nuvem precisa estar vazia')


def deleteHost(family):
    cloud, host = family.split(' - ')
    if multiCloud.deleteHost(host, cloud):
        item = APP.listHosts.currentRow()
        item = APP.listHosts.takeItem(item)
        del item
    else:
        APP.lineNewHost.setPlaceholderText('O host precisa estar vazio')


def deleteVM(family):
    cloud, host, vm = family.split(' - ')
    if multiCloud.deleteVM(vm, host, cloud):
        item = APP.listVMs.currentRow()
        item = APP.listVMs.takeItem(item)
        del item
    else:
        APP.lineNewVM.setPlaceholderText('A VM precisa estar vazia')


def deleteProcess(family):
    cloud, host, vm, process = family.split(' - ')
    multiCloud.deleteProcess(process, vm, host, cloud)

    item = APP.listProcess.currentRow()
    item = APP.listProcess.takeItem(item)
    del item


def migrateHost(family, newFather, itemRow):
    cloud, host = family.split(' - ')

    if multiCloud.migrateHost(host, cloud, newFather):
        APP.listHosts.item(itemRow).setText(newFather + ' - ' + host)

        for row in range(APP.listVMs.count()):
            vmCloud, vmHost, vm = APP.listVMs.item(row).text().split(' - ')
            if vmCloud == cloud and vmHost == host:
                vmFamily = vmCloud + ' - ' + vmHost + ' - ' + vm
                vmNewFather = newFather + ' - ' + host
                migrateVM(vmFamily, vmNewFather, row)
    else:
        APP.lineNewHost.setPlaceholderText('Nome indisponível')


def migrateVM(family, newFather, itemRow, askedFromUser=False):
    cloud, host, vm = family.split(' - ')
    newGFather, newFather = newFather.split(' - ')

    if askedFromUser:
        if multiCloud.migrateVM(vm, host, cloud, newFather, newGFather):
            newFather = newGFather + ' - ' + newFather
            migrateVM(family, newFather, itemRow)
        else:
            APP.lineNewVM.setPlaceholderText('Nome indisponível')
    else:
        APP.listVMs.item(itemRow).setText(newGFather + ' - ' + newFather + ' - ' + vm)

        for row in range(APP.listProcess.count()):
            processCloud, processHost, processVM, process = APP.listProcess.item(row).text().split(' - ')
            if processCloud == cloud and processHost == host and processVM == vm:
                processFamily = processCloud + ' - ' + processHost + ' - ' + processVM + ' - ' + process
                processNewFather = newGFather + ' - ' + newFather + ' - ' + vm
                migrateProcess(processFamily, processNewFather, row)


def migrateProcess(family, newFather, itemRow, askedFromUser=False):
    cloud, host, vm, process = family.split(' - ')
    newGGFather, newGFather, newFather = newFather.split(' - ')

    if askedFromUser:
        if multiCloud.migrateProcess(process, vm, host, cloud, newFather, newGFather, newGGFather):
            APP.listProcess.item(itemRow).setText(newGGFather + ' - ' + newGFather + ' - ' + newFather + ' - ' + process)
        else:
            APP.lineNewProcess.setPlaceholderText('Nome indisponível')
    else:
        APP.listProcess.item(itemRow).setText(newGGFather + ' - ' + newGFather + ' - ' + newFather + ' - ' + process)



# SETUP FUNCTIONS ___________________________________________________________________________________________________
def startApp():
    global APP
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        APP = MainWindow()
        APP.show()
        sys.exit(app.exec())


startApp()
