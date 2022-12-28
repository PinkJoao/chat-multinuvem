from vm import Vm

class Host():
    def __init__(self, father, name):
        self.father = father
        self.name = str(name)
        self.VMs = []

    def addNew(self, name):
        newVm = Vm(self, name)
        self.VMs.append((newVm, name))

    def delete(self, vm):
        if vm in self.VMs:
            self.VMs.remove(vm)

    def add(self, newVM):
        if newVM in self.VMs:
            return False
        else:
            for vm in self.VMs:
                if vm[1] == newVM[1]:
                    return False

            self.VMs.append(newVM)
            return True
            
