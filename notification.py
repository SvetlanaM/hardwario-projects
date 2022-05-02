import time
import datetime
import paho.mqtt.client as paho
from pynput import keyboard


broker="127.0.0.1" # adresa MQTT brokeru
client = paho.Client("meal-notification")


def on_release(key):
        return

def on_message():
        date = datetime.datetime.now()
        #msg = str(message.payload.decode("utf-8")) # Parse zprávy z do klasického stringu

        #if(message.topic == "node/push-button:0/push-button/-/event-count"):    # Podmínka na topic, který je zavolán při stisku tlačítka
        if(date.hour >= 7 and date.hour <= 9):
                print("Prijd na snídani")
        elif(date.hour >= 10 and date.hour <= 13):
                print("Oběd je hotový")
        elif(date.hour >= 17 and date.hour <= 19):
                print("Je čas na večeři")
        #if(message.topic == "node/push-button:0/push-button/-/hold-count"):
        else:
                print("Pojd dolů")

    
def on_press():
        on_message(client, "", "")

def connect():
        global client
        client.on_message=on_message # Nastavení callbacku

        client.connect(broker) # Připojení k MQTT brokeru

        client.loop_start() # Asynchroní čekání na subscribe zprávy
        client.subscribe([("node/push-button:0/push-button/-/event-count",2),("node/push-button:0/push-button/-/hold-count",2)]) # Možné udělat i subscribe na pole
        while True:
                time.sleep(0.2)
        
listener = keyboard.Listener(
    on_press=on_press,
    on_release = on_release)
listener.start()
connect()
