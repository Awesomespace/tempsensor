class ASS_MQTT_DS18B20:
    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

        ap = network.WLAN(network.AP_IF)
        ap.active(False)

        self.ds = DS18X20(OneWire(Pin(ds_pin)))
        devices = self.ds.scan()
        if not devices:
            raise Exception("No DS18B20 devices found")
        self.ds_device = devices.pop()
        print("Found DS18B20 @ ", self.ds_device )

        self.mqtt = MQTTClient(node_id, mqtt_host)

        self.do_connect()

        self.main()

    def do_connect(self):
        if not self.wlan.isconnected():
            print("Connecting to wifi...")
            self.wlan.connect(wifi_ssid, wifi_pass)
            while not self.wlan.isconnected():
                pass
            print("Network config: ", self.wlan.ifconfig())

            print("Connecting to MQTT...")
            while self.mqtt.connect():
                pass
            print("Connected")

    def main(self):
        while True:
            self.ds.convert_temp()
            sleep_ms(750)
            temp = self.ds.read_temp(self.ds_device)

            print("Temperature: %.2f" % temp)
            self.mqtt.publish(mqtt_topic, b"%.2f" % temp)
            sleep(60)


mqtt_ds18b20 = ASS_MQTT_DS18B20()
