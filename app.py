import os
import time
import requests

for j in range(10):
	os.system('echo 1 | sudo dd status=none of=/sys/class/leds/led0/brightness') # led on
	time.sleep(1)
	os.system('echo 0 | sudo dd status=none of=/sys/class/leds/led0/brightness') # led off
	time.sleep(1)

