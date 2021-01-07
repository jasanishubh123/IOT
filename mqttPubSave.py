import psutil
import paho.mqtt.client as mqtt
import time
import sqlite3

DB_NAME = "MessageDB"
con = sqlite3.connect(DB_NAME)
con.execute("CREATE TABLE IF NOT EXISTS usageTB(id INTEGER PRIMARY KEY AUTOINCREMENT,messageTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,message VARCHAR(100))")

def on_connect(client,userdata,flag,rc):
    print(f"connected with result code {rc}")
    
    

client = mqtt.Client()
client.on_connect= on_connect
client.connect("broker.emqx.io",1883,60)

while True:
    mem = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent()
    msg = "RAM - "+str(mem)+" CPU - "+str(cpu)
    cursor = con.cursor()
    cursor.execute("INSERT INTO usageTB(message)values('"+msg+"')")
    con.commit()
    client.publish("rsp/pub",payload=msg,qos=0,retain=False)
    print(f"send message to subscriber- {msg}")
    time.sleep(1)
    
client.loop_forever()