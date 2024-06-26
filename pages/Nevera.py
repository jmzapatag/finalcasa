import paho.mqtt.client as paho
import time
import streamlit as st
import json
values = 0.0
act1="OFF"
from PIL import Image
def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)

        


broker="broker.mqttdashboard.com"
port=1883
client1= paho.Client("NEVERA123")
client1.on_message = on_message
image = Image.open('frio.png')


st.title("Nevera Inteligente ❄️")
st.subheader("Controla aqui tu nevera inteligente ")

if st.button('Prender Luz'):
    act1="ON"
    client1= paho.Client("NEVERA123")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("nevera1z", message)
 
    #client1.subscribe("Sensores")
    
    
else:
    st.write('')

if st.button('Apagar Luz'):
    act1="OFF"
    client1= paho.Client("NEVERA123")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("nevera1z", message)
  
    
else:
    st.write('')

values = st.slider('Cambia la temperatura',-20.0, 20.0)
st.write('Temperatura 🌡️ :', values)

if st.button('Enviar temperatura'):
    client1= paho.Client("NEVERA123")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)   
    message =json.dumps({"Analog": float(values)})
    ret= client1.publish("nevera2z", message)
    
 
else:
    st.write('')

st.image(image)
