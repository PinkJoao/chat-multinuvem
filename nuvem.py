from host import Host

class Cloud():
    def __init__(self, father, name):
        self.father = father
        self.name = str(name)
        self.hosts = []

    def addNew(self, name):
        newhost = Host(self, name)
        self.hosts.append((newhost, name))

    def delete(self, host):
        if host in self.hosts:
            self.hosts.remove(host)

    def add(self, newhost):
        if newhost in self.hosts:
            return False
        else:
            for host in self.hosts:
                if newhost[1] == host[1]:
                    return False

            self.hosts.append(newhost)
            return True
