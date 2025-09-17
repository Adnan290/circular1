import os, sys, io
import M5
from M5 import *
import m5ui
import lvgl as lv
import network 
#import urequests
import machine
import time
# ---------- WiFi & OTA ----------
SSID = "Redmi Note 10"
PASSWORD = "12345678"
URL = "https://raw.githubusercontent.com/Adnan290/circular1/main/main.py"

def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    print("Connecting WiFi...")
    for _ in range(20):
        if wlan.isconnected():
            print("Connected:", wlan.ifconfig())
            return True
        time.sleep(0.5)
    print("WiFi connect failed")
    return False

def ota_update():
    if not wifi_connect():
        return
    try:
        print("Downloading:", URL)
        r = urequests.get(URL)
        if r.status_code == 200:
            with open("main.py", "w") as f:
                f.write(r.text)
            print("Update OK, rebooting...")
            time.sleep(2)
            machine.reset()
        else:
            print("HTTP error:", r.status_code)
        r.close()
    except Exception as e:
        print("OTA failed:", e)
# --------------------------------


page0 = None

def setup():
    global page0
    M5.begin()
    Widgets.setRotation(1)
    m5ui.init()
    page0 = m5ui.M5Page(bg_c=0xffffff)
    page0.screen_load()

def loop():
    global page0
    M5.update()


if __name__ == '__main__':
    print("Starting OTA updater...")
    ota_update()   # will reboot if update succeeds

    # If no update happened, start UI
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            m5ui.deinit()
            from utility import print_error_msg
            print_error_msg(e)
        except ImportError:
            print("please update to latest firmware")
