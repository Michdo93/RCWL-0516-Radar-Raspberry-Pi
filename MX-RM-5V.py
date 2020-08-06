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

tx = piVirtualWire.tx(pi, tx_module_gpio_pin, baud_rate)

msg = "42"

tx.put(msg)
tx.waitForReady()

tx.cancel()
pi.stop()