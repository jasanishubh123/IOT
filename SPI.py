import spidev
import time

spi=spidev.SpiDev(0,1)
spi.open(0,1)
# msg=0xAA

spi.max_speed_hz=115200
while 1:
    spi.writebytes([0x4,0x48])
    y=spi.readbytes(1)
    print(str(y))
    time.sleep(0.5)
    