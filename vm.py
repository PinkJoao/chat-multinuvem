from processo import Process

class Vm():
    def __init__(self, father, name):
        self.father = father
        self.name = str(name)
        self.process = []

    def addNew(self, name):
        newProcess = Process(self, name)
        self.process.append((newProcess, name))

    def delete(self, process):
        if process in self.process:
            self.process.remove(process)
            process[0].flag = False

    def add(self, newProcess):
        if newProcess in self.process:
            return False
        else:
            for process in self.process:
                if process[1] == newProcess[1]:
                    return False

            self.process.append(newProcess)
            return True
