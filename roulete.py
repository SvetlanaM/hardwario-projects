#import all needed libraries
import time
import random
import paho.mqtt.client as paho

#Here goes IP address of your mqtt broker
#If you are running it on this computer leave it as is
broker="127.0.0.1"

#define variables
contestants = []
currContestant = ""
firstConnecting = True

#define callback
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    
    if(message.topic == "node/push-button:0/orientation"):
        shuffle()
    elif(message.topic == "node/push-button:0/push-button/-/event-count"):
        choose()
    elif(message.topic == "node/push-button:0/push-button/-/hold-count"):
        reset()
    

def shuffle():
    print("micham")
    random.shuffle(contestants)


def choose():
    print(contestants)
    for x in range(3):
        print('Vybiram.')
        time.sleep(1)
        print("Vybiram..")
        time.sleep(1)
        print("Vybiram...")
        time.sleep(1)
    
    print("Vybral jsem: ", random.choice(contestants))


def reset():
    contestants.clear()
    addContestants()


def connect():
    client= paho.Client("roullete")
    client.on_message=on_message

    client.connect(broker)#connect

    client.loop_start() #start loop to process received messages
    client.subscribe([("node/push-button:0/push-button/-/event-count",2),("node/push-button:0/push-button/-/hold-count",1),("node/push-button:0/orientation", 0)])
    while 1:
        time.sleep(0.2)

def addContestants():
    global firstConnecting
    while True:
        currContestant = input("Zadejte jméno účastníka: ")
        if currContestant in contestants:
            print("Toto jméno již seznam obsahuje.")
            continue
        elif(currContestant != ''):
            contestants.append(currContestant)
        else:
            break
    if (firstConnecting):
        firstConnecting = False
        connect()

addContestants()


