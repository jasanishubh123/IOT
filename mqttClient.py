import paho.mqtt.client as mqtt
import sqlite3

DB_NAME="MqttDB.db"
conn=sqlite3.connect(DB_NAME)

def on_connect(client,userdat,flag,rc):
    print(f"connected with {rc}")
    client.subscribe("rsp/pub")
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS mqttMessage(id INTEGER PRIMARY KEY AUTOINCREMENT ,mtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,msg VARCHAR(100))')
    
def on_message(client,userdata,msg):
    print(f"Mesage from is - {msg.topic} and msg - {msg.payload}")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO mqttMessage(msg)values('"+str(msg.payload.decode('UTF-8'))+"')")
    conn.commit()
    
client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message

client.connect("broker.emqx.io",1883,60)
client.loop_forever()
