import json
import time
# need to install paho-mqtt by: 'pip install paho-mqtt'
import paho.mqtt.client as mqtt

# Smart Light Bulb Class for the simulated light bulb
class SmartLightBulb:

    # Initialize the light bulb to default status

    def __init__(self):
        self.state = "off"
        self.brightness = 0

    # Setters and getters for the state and brightness

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_brightness(self, brightness):
        self.brightness = brightness

    def get_brightness(self):
        return self.brightness

    # Can add more details to the light bulb class here if needed
    # e.g. if brightness is 0, then the light bulb is off
    # e.g. if brightness is positive, then the light bulb is on




# MQTT Client Callbacks for connection and messages
# instruction message as json {"state": "on", "brightness": 50}
# home/lightbulb/set is the topic for instruction

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("home/lightbulb/set")

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload)
    if "state" in payload:
        light_bulb.set_state(payload["state"])
    if "brightness" in payload:
        light_bulb.set_brightness(payload["brightness"])
    publish_status()

# Publish light bulb status to MQTT broker
def publish_status():
    status = {
        "state": light_bulb.get_state(),
        "brightness": light_bulb.get_brightness()
    }
    client.publish("home/lightbulb/status", json.dumps(status))



# Initialize the simulated light bulb and MQTT client
light_bulb = SmartLightBulb()
client = mqtt.Client()

# Set MQTT callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
# change the domain name to designated MQTT broker
client.connect("mqtt-domain.com", 1883, 60)

# Loop and process MQTT messages
try:
    client.loop_start()
    while True:
        # check every second for update
        time.sleep(1)
        # print current light bulb status
        print(f"Light Bulb Status: {light_bulb.get_state()}, {light_bulb.get_brightness()}")

except KeyboardInterrupt:
    print("exitting...")
finally:
    # shut down the MQTT client and disconnect
    client.loop_stop()
    client.disconnect()
