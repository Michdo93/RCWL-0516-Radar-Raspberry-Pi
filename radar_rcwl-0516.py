import os
import sys
import getpass
import time
import pigpio
import RPi.GPIO as GPIO

# #include <VirtualWire.h>

env=os.path.expanduser(os.path.expandvars('/home/' + getpass.getuser() + '/robotcar/lib'))
sys.path.insert(0, env)

import piVirtualWire.piVirtualWire as piVirtualWire

PIN_RADAR = 4 # #define PIN_RADAR 2
PIN_TX = 17 # #define PIN_TX 9
# PIN_LED = 13 # #define PIN_LED 13 # print instead

# void setup()
baud_rate = 1000 # baud rate instead of bps connection speed

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_RADAR, GPIO.IN)
# GPIO.setup(PIN_LED, GPIO.OUT)

# not needed
# pinMode(PIN_LED, OUTPUT);

pi = pigpio.pi()

# vw_set_tx_pin(PIN_TX); # and
# vw_setup(6000);
tx = piVirtualWire.tx(pi, PIN_TX, baud_rate)

rv = -1 # int rv = -1; # "unused"

try:
	# void loop()
	while True:
		#print("PIN_LED would be HIGH if you want to use it")
		# GPIO.output(PIN_LED, GPIO.HIGH) # LED on # digitalWrite(PIN_LED, HIGH);
		v = GPIO.input(PIN_RADAR) # int v = digitalRead(PIN_RADAR);

		if(v != rv):
			rv = v
			# char msg[20];
			# sprintf(msg, "R %lu %d", millis() / 1000, v);
			msg = "R %f %d" % (time.time(), v)
			tx.put(msg) # vw_send((uint8_t *)msg, strlen(msg));
			print(msg) # Serial.println(msg);
			tx.waitForReady() # vw_wait_tx();
		#print("PIN_LED would be LOW if you want to use it")
		# GPIO.output(PIN_LED, GPIO.LOW) # LED off # digitalWrite(PIN_LED, LOW);
		time.sleep(0.1)
		
except KeyboardInterrupt: # press Ctrl + C to stop
	GPIO.cleanup()
	tx.cancel()
	pi.stop()