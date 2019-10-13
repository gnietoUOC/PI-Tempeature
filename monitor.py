import sys
import time
#import json
from datetime import datetime

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
		now = datetime.now()
		topic = str(message.topic)
		payload = str(message.payload.decode("UTF-8"))
		data = payload.split(",")

		try:
#			print(now,data[1])
#			print(datetime.strptime(now,"%Y-%m-%d %H:%M:%S.%f"))
#			print(datetime.strptime(data[1],"%Y-%m-%d %H:%M:%S.%f"))
#			print(datetime.strptime(now))
#			delta = datetime.strptime(now,"%Y-%m-%d %H:%M:%S.%f")-datetime.strptime(data[1],"%Y-%m-%d %H:%M:%S.%f") 
			delta = now-datetime.strptime(data[1],"%Y-%m-%d %H:%M:%S.%f") 
			
			print ("{}\t{} ({}) - {}:{}".format(datetime.now(),data[1],delta,topic,data[0]))
		except:
			print("Oh!")

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

