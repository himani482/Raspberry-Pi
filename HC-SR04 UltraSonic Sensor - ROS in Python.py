import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
TRIGGER  = 15
ECHO = 18


gpio.setup(TRIGGER,gpio.OUT)
gpio.setup(ECHO,gpio.IN)

try:
  while True:
    gpio.output(TRIGGER,1)
    time.sleep(0.00001)
    gpio.output(TRIGGER,0)
    start= 0
    stop=0
    
    while gpio.input(ECHO) ==0:
      start = time.time()
    while gpio.input(ECHO)==1:
      stop = time.time()
    Total_time= stop - start
    Distance= (34300 * Total_time )/2
    print(f"Distance: {distance} cm")
except:
  print("Done")
finally:
  gpio.cleanup()
