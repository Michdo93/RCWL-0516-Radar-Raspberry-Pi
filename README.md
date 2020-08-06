# RCWL-0516-Radar-Raspberry-Pi

You can get furteher informations here: https://hackaday.io/project/19400-first-steps-with-the-rcwl-0516-radar-switch

Or in the [https://img.filipeflop.com/files/download/Datasheet_rcwl-0516.pdf](datasheet).

You also need [https://github.com/DzikuVx/piVirtualWire](piVirtualWire).


## DESCRIPTION
The RCWL-0516 module can be bought at numerous online retailers on eBay and Aliexpress, as well as others. It's intended for lamps and wall lights, where it can turn them on when motion is detected, and turn them off after a short timeout. Short-range (~~5m) radar modules such as this one are an alternative to PIR (passive infra-red) modules. Despite it being a very wide-spread and cheap module, documentation is scarce.

## DETAILS
The module's pinout seems to be:

* 3V3 - module power supply
* GND - common ground
* OUT - outgoing light voltage
* IN - incoming light voltage
* CDS - light detect / module disable feature

As far as I can currently tell, it works something like this: if the CDS is not pulled low, the module will send out pulses and measure their return times. If a change in return times is detected (i.e. something in the path of the radio waves has changed position), it will connect the IN and OUT lines (most likely with a MOSFET). So if there's a light connected to the OUT line, and an external power source (4V - 28V) is connected to IN, it will light up. The OUT line will go low after a short period of time (a few seconds) if movement stops. Of course, GND lines must be connected together.

I'll need to experiment with it some more.

## FILES

* radar_rcwl-0516.py
It's the developed Python program.
* FS1000A.py
piVirtualWire test File
* MX-RM-5V.py
piVirtuaelWire test File

## COMPONENTS

* 1 × RCWL-0516 Microwave Radar Sensor Module
Can be bought from numerous online vendors at a price of $1-$2.
* 1 × Raspberry Pi
Of your favourite flavour
* 1 × XY-FST 433 MHz ASK transmitter
If you want to run the attached sketch literally
