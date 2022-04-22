import vlc
import time
import os
import paho.mqtt.client as paho

playlist = []

#Here goes IP address of your mqtt broker
#If you are running it on this computer leave it as is
broker="127.0.0.1"

#define callback
def on_message(client, userdata, message):
    message = str(message.payload.decode("utf-8"))

    if(message == "play"):
        for song in playlist:
            player = vlc.MediaPlayer(song)
            player.play()
            time.sleep(1)
            print(player.get_state())
            time.sleep(player.get_length() / 1000)

    elif(message == "stop"):
        player.stop()


def connect():
    client= paho.Client("music-player")
    client.on_message=on_message

    client.connect(broker)#connect

    client.loop_start() #start loop to process received messages
    client.subscribe("favourite/playlist/action")#subscribe
    while 1:
        time.sleep(0.2)
        

for r, d, f in os.walk("C:/Users/Kubaa/Music/"):
    for file in f:
        if '.mp3' in file:
            playlist.append(os.path.join(r, file))
print(playlist)
connect()
