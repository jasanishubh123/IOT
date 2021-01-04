import paho.mqtt.client as mqtt
import time

def on_connect(client,userdata,flag,rc):
    print(f"connected with result code {rc}")
    
client=mqtt.Client()
client.on_connect=on_connect
client.connect("10.25.4.148",1883,60)

while True:
    inp=input("Enter your message:")
    client.publish("rsp/pub",payload=inp,qos=0,retain=False)
    print(f"send to rsp/pub")
    time.sleep(1)
    
client.loop_forever()