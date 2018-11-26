import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

l1 = 2
l2 = 3
l3 = 4
l4 = 5

mqtt_username = "pi"
mqtt_password = "raspberry"
mqtt_topic = "project"
mqtt_broker_ip = "192.168.43.217"

GPIO.setmode(GPIO.BOARD)

client = mqtt.Client()
client.username_pw_set(mqtt_username, mqtt_password)
def on_connect(client, userdata, flags,rc):
    print ("Connected!", str(rc))
    client.subscribe(mqtt_topic)
    
def on_message(client, userdata,msg):    
    print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
    if str(msg.payload) == "b'on1'":
        GPIO.output(l1, ON)
    elif str(msg.payload) == "b'off1'":
        GPIO.output(l1, OFF)
    elif str(msg.payload) == "b'on2'":
        GPIO.output(l2, ON)
    elif str(msg.payload) == "b'off2'":
        GPIO.output(l2, OFF)
    elif str(msg.payload) == "b'on3'":
        GPIO.output(l3, ON)
    elif str(msg.payload) == "b'off3'":
        GPIO.output(l3, OFF)
    elif str(msg.payload) == "b'on4'":
        GPIO.output(l4, ON)
    elif str(msg.payload) == "b'off4'":
        GPIO.output(l4, OFF)
        
    
        
        
    
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_broker_ip, 1883)

client.loop_forever()
client.disconnect()
