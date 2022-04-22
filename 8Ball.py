#import all needed libraries
import time
import random
import paho.mqtt.client as paho

#Here goes IP address of your mqtt broker
#If you are running it on this computer leave it as is
broker="127.0.0.1"

#define variables
answers = ["It is certain.", "It is decidedly so.", "Without a doubt.",
           "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
           "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
           "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
           "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.",
           "My reply is no.", "My sources say no.", "Outlook not so good.","Very doubtful."]

#define callback
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    
    random.shuffle(answers)
    print("The answer is: ", random.choice(answers))

    time.sleep(3)

    print("You can ask me again and shake!")

def connect():
    client= paho.Client("8-ball")
    client.on_message=on_message

    client.connect(broker)#connect

    client.loop_start() #start loop to process received messages
    client.subscribe("node/future-teller:0/future/trigger")
    while 1:
        time.sleep(0.2)
print("Ask me any Yes/No question and shake the module!")
connect()


