import paho.mqtt.client as mqtt
import json
import base64
import binascii



def on_connect(client, userdata, flags, rc):

    print("Connected with result code "+str(rc))
    client.subscribe("lora/+/up")


def on_message(client, userdata, msg):
    
    print("Topic: ", msg.topic+'\nMessage: '+str(msg.payload))
    #BT - Extract out the mac address in the topic
    mac_node = msg.topic.split('/')
    print("BT - mac_node: " + mac_node[1])
    #BT - Convert to json format data structure
    json_data = json.loads(msg.payload.decode("utf-8"))
    topic_down = "lora/" + mac_node[1] + "/down"
    print("BT - Topic down: " + topic_down)
    print("BT - json_data: %s" %(json_data["data"]))
    data_to_mDot = "{ \"data\": \"" + json_data["data"] + "\" }"
    print("BT - data_to_mDot: " + data_to_mDot)
    client.publish(topic_down,data_to_mDot)
    
    # Decode Base64 to bytes
    base64_payload = json_data["data"]
    decoded_bytes = base64.b64decode(base64_payload)
    
    # Convert bytes to hexadecimal
    hex_payload = binascii.hexlify(decoded_bytes).decode("utf-8")
    print("BT - Hexadecimal Payload: " + hex_payload)



client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
client.connect("127.0.0.1", 1883, 60)
client.loop_forever()
