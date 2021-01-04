import spidev
import time

spi = spidev.SpiDev(0,0)
spi.open(0, 0)
spi.max_speed_hz = 115200
while 1:
        #resp = spi.xfer2([0xAA,spi.max_speed_hz,3])
        spi.writebytes([0x4, 0x06])
        y = spi.readbytes(32)
        if y[0]!=0:
            print("Aurdino Connected")
            print(y)
        time.sleep(1)