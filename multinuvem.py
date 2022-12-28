from nuvem import Cloud

class MultiCloud():
    def __init__(self):
        self.clouds = []

    def searchCloud(self, name):
        for cloud in self.clouds:
            if cloud[1] == name:
                return cloud

    def searchHost(self, name, cloud):
        cloud = self.searchCloud(cloud)
        
        for host in cloud[0].hosts:
            if host[1] == name:
                return host

    def searchVM(self, name, host, cloud):
        host = self.searchHost(host, cloud)

        for vm in host[0].VMs:
            if vm[1] == name:
                return vm

    def searchProcess(self, name, vm, host, cloud):
        vm = self.searchVM(vm, host, cloud)

        for process in vm[0].process:
            if process[1] == name:
                return process
            

    def addNewCloud(self, cloudName):
        if self.searchCloud(cloudName):
            return False
        else:
            newCloud = Cloud(self, cloudName)
            self.clouds.append((newCloud, cloudName))
            return True

    def addNewHost(self, hostName, cloud):
        if self.searchHost(hostName, cloud):
            return False
        else:
            cloud = self.searchCloud(cloud)
            cloud[0].addNew(hostName)
            return True

    def addNewVM(self, vmName, host, cloud):
        if self.searchVM(vmName, host, cloud):
            return False
        else:
            host = self.searchHost(host, cloud)
            host[0].addNew(vmName)
            return True

    def addNewProcess(self, processName, vm, host, cloud):
        if self.searchProcess(processName, vm, host, cloud):
            return False
        else:
            vm = self.searchVM(vm, host, cloud)
            vm[0].addNew(processName)
            return True

    def deleteCloud(self, cloudName):
        cloud = self.searchCloud(cloudName)
        if cloud[0].hosts == []:
            self.clouds.remove(cloud)
            return True
        else:
            return False

    def deleteHost(self, host, cloud):
        host = self.searchHost(host, cloud)
        if host[0].VMs == []:
            host[0].father.delete(host)
            return True
        else:
            return False

    def deleteVM(self, vm, host, cloud):
        vm = self.searchVM(vm, host, cloud)
        if vm[0].process == []:
            vm[0].father.delete(vm)
            return True
        else:
            return False

    def deleteProcess(self, process, vm, host, cloud):
        process = self.searchProcess(process, vm, host, cloud)
        process[0].father.delete(process)
       
    def migrateHost(self, host, cloud, newFather):
        host = self.searchHost(host, cloud)
        newFather = self.searchCloud(newFather)
        if newFather[0].add(host):
            host[0].father.delete(host)
            host[0].father = newFather[0]
            return True
        else:
            return False

    def migrateVM(self, vm, host, cloud, newFather, newGFather):
        vm = self.searchVM(vm, host, cloud)
        newFather = self.searchHost(newFather, newGFather)
        if newFather[0].add(vm):
            vm[0].father.delete(vm)
            vm[0].father = newFather[0]
            return True
        else:
            return False

    def migrateProcess(self, process, vm, host, cloud, newFather, newGFather, newGGFather):
        process = self.searchProcess(process, vm, host, cloud)
        newFather = self.searchVM(newFather, newGFather, newGGFather)
        if newFather[0].add(process):
            process[0].father.delete(process)
            process[0].father = newFather[0]
            return True
        else:
            return False

