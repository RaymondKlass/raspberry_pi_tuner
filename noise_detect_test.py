import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)


def getAdc(channel):
    # check for valid channel
    if ((channel > 7) or (channel < 0)):
        return -1

    # Preform SPI transaction and store returned bits in 'r'
    r = spi.xfer([1, (8 + channel) << 4], 0)

    #adcOut = ( (r[1] & 3) << 8 ) + r[2]

    #print("ADCOut: {}".format(adcOut))
    print("R Value: {}".format(r))
    
for i in range(100):
    start = time.time()
    getAdc(0)
    print("Delay: {}".format(time.time() - start))
