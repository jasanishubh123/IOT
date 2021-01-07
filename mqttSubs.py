import paho.mqtt.client as mqtt


def on_connect(client,userdata,flag,rc):
    print(f"connected with {rc}")
    client.subscribe("rsp/pub")

def on_message(client,userdata,msg):
    print(f"Message from Publisher {str(msg.payload.decode('utf-8'))}")
    

client = mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message

client.connect("broker.emqx.io",1883,60)
client.loop_forever()