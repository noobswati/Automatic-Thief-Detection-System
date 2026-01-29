import paho.mqtt.client as mqtt
from camera_capture import capture_image

BROKER_IP = "BROKER_IP"

def on_message(client, userdata, msg):
    if msg.payload.decode() == "MOTION_DETECTED":
        print("Motion detected! Capturing image...")
        image_path = capture_image()
        client.publish("thief/image", image_path)

client = mqtt.Client()
client.connect(BROKER_IP, 1883)
client.subscribe("thief/detection")
client.on_message = on_message

print("MQTT Subscriber running...")
client.loop_forever()
