from flask import Flask, render_template
import paho.mqtt.client as mqtt

app = Flask(__name__)
latest_image = None

def on_message(client, userdata, msg):
    global latest_image
    latest_image = msg.payload.decode()

client = mqtt.Client()
client.connect("BROKER_IP", 1883)
client.subscribe("thief/image")
client.on_message = on_message
client.loop_start()

@app.route("/")
def index():
    return render_template("index.html", image=latest_image)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
