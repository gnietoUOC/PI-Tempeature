import sys
import time
#import json
import paho.mqtt.client as mqtt
from gpiozero import CPUTemperature
from datetime import datetime

class MQTTControl:


	def __init__(self,name):
		self.mqttc = mqtt.Client(name)
		self.mqttc.connect("test.mosquitto.org",1883)
		self.i = 0
	
	def send(self,topic,data):
		message = ','.join(str(e) for e in [data,datetime.now(),self.i])
		self.i = self.i + 1	
		self.mqttc.publish(topic,message)

	def __del__(self):
		self.mqttc.disconnect()


def main():
	control = MQTTControl("pi3b")
	
	while(1):
		cpu = CPUTemperature()
		temp = cpu.temperature
		print("{}".format(temp))
		control.send("GNFPiTemp",temp);
		time.sleep(1)
			
	del control

if __name__ == "__main__":
	sys.exit(main())


