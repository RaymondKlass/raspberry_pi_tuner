import spidev
import os

spi = spidev.SpiDev()
spi.open(0,0)

print("Yay")
