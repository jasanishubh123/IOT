from smbus import SMBus
addr=0x8
bus = SMBus(1)
numb=1

print("Enter 1 for ON or 0 for OFF")
while numb ==1:
    ledstate=input("Enter input: ")
    if ledstate == "1":
        bus.write_byte(addr,0x1)
        block = bus.read_byte_data(8,1)
        print(block)
        
    elif ledstate == "0":
            bus.write_byte(addr,0x0)
    else:
            numb = 0