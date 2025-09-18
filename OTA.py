import os, sys, io
import M5
from M5 import *
import m5ui
import lvgl as lv



page0 = None
label0 = None


def setup():
  global page0, label0

  M5.begin()
  Widgets.setRotation(1)
  m5ui.init()
  page0 = m5ui.M5Page(bg_c=0xffffff)
  label0 = m5ui.M5Label("label0", x=166, y=58, text_c=0x000000, bg_c=0xffffff, bg_opa=0, font=lv.font_montserrat_14, parent=page0)

  page0.screen_load()


def loop():
  global page0, label0
  M5.update()
  label0.set_text(str('ADNAN'))


if __name__ == '__main__':
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
