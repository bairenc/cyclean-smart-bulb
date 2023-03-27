1. Install paho-mqtt by: 

```linux
pip install paho-mqtt
```

2. Sub in MQTT Server info for line 71 (for now just used example for mqtt lib)
    
```python
    # Connect to the MQTT broker
    # change the domain name to designated MQTT broker
    client.connect("mqtt-domain.com", 1883, 60)
```

Contact: Andy Chen (Chenandy@usc.edu)
