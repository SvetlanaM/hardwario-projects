import vlc
import time
import paho.mqtt.client as paho

player = vlc.MediaPlayer("C:/Users/Kubaa/Music/02 - After the Disco.mp3")


#Here goes IP address of your mqtt broker
#If you are running it on this computer leave it as is
broker="127.0.0.1"

#define callback
def on_message(client, userdata, message):
    message = str(message.payload.decode("utf-8"))

    global player

    player.stop()

    print(message)
    
    if(message == "1"):
        player = vlc.MediaPlayer("C:/Users/Kubaa/Music/02 - After the Disco.mp3")

    elif(message == "2"):
        player = vlc.MediaPlayer("C:/Users/Kubaa/Music/01 - Perfect World.mp3")

    player.play()

def connect():
    client= paho.Client("music-player")
    client.on_message=on_message

    client.connect(broker)#connect

    client.loop_start() #start loop to process received messages
    client.subscribe("node/push-button:0/orientation")#subscribe
    while 1:
        time.sleep(0.2)
        
connect()
