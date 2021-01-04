import context
import paho.mqtt.client as client
import sqlite3

connection = sqlite3.connect("mqtt.db")
sql_command = "CREATE TABLE IF NOT EXISTS mqtt(id INTEGER PRIMARY KEY AUTOINCREMENT, time DATETIME DEFAULT CURRENT_TIMESTAMP, msg VARCHAR(10))"
cursor = connection.cursor()
connection.execute(sql_command)

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("ass")

def save_message(msg):
    sql = "INSERT INTO mqtt(msg) VALUES('"+msg+"');"
    cursor.execute(sql);
    row = cursor.execute('select * from mqtt')
    for row in cursor:
        print(row[0], row[1], row[2])
    #print(total)

def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload}")
    save_message(msg.payload.decode());
    client.publish(topic="ret",payload="Viraj",qos=1,retain=False)
    
client = client.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.emqx.io", 1883, 60)
client.publish(topic="ret",payload="Viraj",qos=1,retain=False)

client.loop_forever()
