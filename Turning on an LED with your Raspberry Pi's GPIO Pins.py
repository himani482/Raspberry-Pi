import RPi.GPIO as gpio
import time
import sys

usage="""
usage:led <state>
STATES:
  on = "turn on the led"
  off=" turn off the led"
  blink=" set the bilinking mode for led"
"""
gpio.setwarnings(False)
if len(sys.argv) <2:
  print(usage)
  exit()
state = sys.argv[1]
gpio.setmode(gpio.BCM)
gpio.setup(24,gpio.OUT) #  for gpio pin 24
if state == "on":
  gpio.output(24,1)  # turn on the led
elif state == "off":
  gpio.output(24,0)  # turn off the led
elif state =="blink":
  while True:
    gpio.output(24,1)
    time.sleep(0.5)
    gpio.output(24,0)
  
else:
  print(usage)
  exit()
