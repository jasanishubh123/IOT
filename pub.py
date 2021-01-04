#import context
import paho.mqtt.client as mqtt

def on_connect(client,userdata,flags,rc):
    print("Connected with result code{rc}")
    client.subscribe('ret');

def on_message(client,userdata,msg):
    print("Message"+ msg.payload.decode())
    client.publish(topic="test",payload="Viraj",qos=1,retain=False)
    
client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
client.connect("broker.emqx.io",1883)
client.publish(topic="test",payload="Viraj",qos=1,retain=False)
client.loop_forever()

