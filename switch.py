# Python script to control LIFX lightbulb over LAN

import RPi.GPIO as GPIO
import time
import sys

from lifxlan import LifxLAN

def main():

  # Definitions for the Floral Bonnet extension   
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  # Object representation of the LAN network
  lan = LifxLAN()
  light = lan.get_device_by_name("Room")

  while True:
     input_state = GPIO.input(4)
     if input_state == False:
          try:
               state = light.get_power()
               if state == 65535:	
                    lan.set_power_all_lights(0)
               else:
                    lan.set_power_all_lights(65535)
          except:
               continue


if __name__ == '__main__':
     main()