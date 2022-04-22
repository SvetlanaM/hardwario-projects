import vlc
import time
import paho.mqtt.client as paho
from pynput import keyboard

alarmState = 0


#Here goes IP address of your mqtt broker
#If you are running it on this computer leave it as is
broker="127.0.0.1"
client = paho.Client("burglar-alarm")


def on_press(key):
    global client
    if key == keyboard.Key.space:
        global alarmState
        if(alarmState == 0):
                alarmState = 1
        else:
                alarmState = 0
        print(alarmState)


def on_release(key):
    return 
    

#define callback
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    if(message.topic == "node/burglar-alarm:0/thermometer/0:1/temperature"):
            client.publish("node/burglar-alarm:0/alarm/-/set/state", alarmState)
            print(alarmState)
        
    elif(message.topic == "node/burglar-alarm:0/pir/-/event-count"):
            player = vlc.MediaPlayer("C:/Users/Kubaa/Desktop/Hardwario/Sci-Fi Sound Effect - Intruder Alert.mp3")
            player.play()
            print("alarm")
    

def connect():
    global client
    client.on_message=on_message

    print("connecting to broker ",broker)
    client.connect(broker)#connect

    client.loop_start() #start loop to process received messages
    print("subscribing ")
    client.subscribe([("node/burglar-alarm:0/thermometer/0:1/temperature",2),("node/burglar-alarm:0/pir/-/event-count",1)])
    while 1:
        time.sleep(0.2)
        
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
connect()
