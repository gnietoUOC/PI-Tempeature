import sys
import time

import paho.mqtt.client as mqtt

class MQTTControl:

	def __init__(self,name):
		self.mqttc = mqtt.Client(name)
		self.mqttc.connect("test.mosquitto.org",1883)
		self.mqttc.on_message = self.read
		self.mqttc.loop_start()

	def listen(self,topic):
		self.mqttc.subscribe(topic)

	def read(self,client,userdata,message):
		topic = str(message.topic)
		message = str(message.payload.decode("UTF-8"))
		print ("{}:{}".format(topic,message))

	def __del__(self):
		self.mqttc.disconnect()


def main():

	control = MQTTControl("ubuntu1904")
	control.listen("GNFPiTemp")

	while(1):
		time.sleep(10)

	del control

if __name__ == '__main__':
	sys.exit(main())

