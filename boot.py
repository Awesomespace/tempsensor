import esp, network
from umqtt.robust import MQTTClient
from ds18x20 import DS18X20
from machine import Pin
from onewire import OneWire
from time import sleep_ms, sleep

node_id = "vrieskist"

wifi_ssid = "ASS"
wifi_pass = "eurosnoeren"

mqtt_host = "statsdingen.ass"
mqtt_topic = "ass/temperature/%s/state" % node_id

ds_pin = 4
