from threading import Thread
from threading import Event
from time import sleep

from client import MQClient

class Process():
    def __init__(self, father, name):
        self.father = father
        self.name = str(name)
        self.messages = []

        self.window = None

        self.flag = True
        self.client = None
        
        self.thread = Thread(target= self.startClient)
        self.thread.start()
        

    def startClient(self):
        self.client = MQClient(self, 'multinuvens')
        self.client.start()
        self.client.client.unsubscribe()

    def sendMessage(self, message):
        self.client.publish(message)
    
