#import knihoven
import vlc
import time
import datetime
import paho.mqtt.client as paho
 
#Nastavení proměnných
broker="127.0.0.1" # adresa MQTT brokeru
client = paho.Client("meal-notification") # Název clienta
 
#Callback, který se zavolá při příjmutí zprávy na topicu, na který je subscribe
def on_message(client, userdata, message):
        date = datetime.datetime.now() #Přiřazení hodnoty proměnné 
        msg = str(message.payload.decode("utf-8")) # Parse zprávy z do klasického stringu
        
        player = vlc.MediaPlayer("C:/Users/Kubaa/Desktop/Hardwario/Reception Bell Chime Sound Effect.mp3")
        player.play()
 
        if(message.topic == "node/push-button:0/push-button/-/event-count"):    # Podmínka na topic, který je zavolán při stisku tlačítka
                if(date.hour >= 7 and date.hour <= 9): #odsazování do bloků | vnořená podmínka
                        print("Je %d hodin %d minut, prijd na snídani" % (date.hour, date.minute))
                elif(date.hour >= 10 and date.hour <= 13): #Výraz s logickým operátorem | elif
                        print("Je %d:%d, oběd je hotový" % (date.hour, date.minute))
                elif(date.hour >= 17 and date.hour <= 19):
                        print("Je %d hodin a čas na večeři" % date.hour)
        if(message.topic == "node/push-button:0/push-button/-/hold-count"): # Tady se dá na ukázku dát else místo dalšího if
                print("Pojd dolů") #Výpis na obrazovku
def connect():
        global client #globální proměnná
        client.on_message=on_message # Nastavení callbacku
 
        client.connect(broker) # Připojení k MQTT brokeru
 
        client.loop_start() # Asynchroní čekání na subscribe zprávy
        client.subscribe([("node/push-button:0/push-button/-/event-count",2),("node/push-button:0/push-button/-/hold-count",2)]) # Možné udělat i subscribe na pole
        while True: # Cyklus While(nekonečný cyklus)
                time.sleep(0.2)
#volání funkce
connect()
