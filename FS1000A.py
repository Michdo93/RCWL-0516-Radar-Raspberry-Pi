import os
import sys
import getpass
import time
import pigpio

env=os.path.expanduser(os.path.expandvars('/home/' + getpass.getuser() + '/robotcar/lib'))
sys.path.insert(0, env)

import piVirtualWire.piVirtualWire as piVirtualWire

pi = pigpio.pi()
tx_module_gpio_pin = 17
baud_rate = 1000

rx = piVirtualWire.rx(pi, tx_module_gpio_pin, baud_rate)

while True:

		print("rx not ready")

		while rx.ready():
			print("RX-Get: " + rx.get())

		time.sleep(0.5)

rx.cancel()
pi.stop()
