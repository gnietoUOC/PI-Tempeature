import sys
import time

import paho.mqtt.client as mqtt
from gpiozero import CPUTemperature

class MQTTControl:


	def __init__(self,name):
		self.mqttc = mqtt.Client(name)
		self.mqttc.connect("test.mosquitto.org",1883)
	
	def send(self,topic,message):
		self.mqttc.publish(topic,message)

	def __del__(self):
		self.mqttc.disconnect()


def main():
	control = MQTTControl("pi3b")
	
	while(1):
		cpu = CPUTemperature()
		temp = cpu.temperature
		print("{}\n".format(cpu.temperature))
		control.send("GNFPiTemp",temp);
		time.sleep(1)
			
	del control

if __name__ == "__main__":
	sys.exit(main())


