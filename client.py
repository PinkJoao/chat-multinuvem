from paho.mqtt import client as mqtt_client
from time import sleep

class MQClient():
    def __init__(self, process, username, password = 'public'):

        self.broker = 'broker.hivemq.com'
        self.port = 1883

        self.process = process
        self.topic = process.father.father.father.name + ' - ' + process.father.father.name + ' - ' + process.father.name
        self.messages = process.messages

        self.id = process.father.father.father.name + ' - ' + process.father.father.name + ' - ' + process.father.name + ' - ' + process.name
        self.username = username
        self.password = password
        self.flag = process.flag
        self.client = None


    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_disconnect(self, client, userdata, rc):
        if rc == 0:
            print('Connection terminated!')

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print('Subscribed to:', str(mid), str(granted_qos))
        

    def on_message(self, client, userdata, message):
        msg =str(message.topic) + ' - ' + str(message.payload.decode('utf-8'))
        self.messages.append(msg)
        try:
            self.process.window.updateMessages()
        except:
            pass
        

    def publish(self, message):
        message = self.process.name + ':' + message
        self.client.publish(self.process.father.father.father.name + ' - ' + self.process.father.father.name + ' - ' + self.process.father.name, message)
        self.process.window.updateMessages()


    def start(self):
        self.client = mqtt_client.Client(self.id)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_subscribe = self.on_subscribe
        self.client.on_message = self.on_message
        self.client.connect(self.broker, self.port)

        sleep(0.5)

        self.client.loop_start()
        self.client.subscribe(self.topic)

        sleep(0.5)

        while self.flag:
            if self.flag == False:
                break
            elif self.topic != self.process.father.father.father.name + ' - ' + self.process.father.father.name + ' - ' + self.process.father.name:
                self.client.unsubscribe(self.topic)
                sleep(1)
                self.topic = self.process.father.father.father.name + ' - ' + self.process.father.father.name + ' - ' + self.process.father.name
                self.client.subscribe(self.topic)
                sleep(0.5)

        self.client.disconnect()
        self.client.loop_stop

    def resub(self, sub):
        print('reincrevendo')
        self.client.unsubscribe(self.topic)
        self.client.subscribe(sub)
        self.topic = sub

   
        

    