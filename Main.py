from SerialPortManager import*
import json

# loop
while True:
    
    msg = ''
    
    # read msg from XBee
    while True:
        msg = SerialPortManager().readMsg()
        if msg != '':
            print(msg.strip())
            #print (msg)
            break
    
    # doRequest
    #PNPRequest(msg).doRequest()