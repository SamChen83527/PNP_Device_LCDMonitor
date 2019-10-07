import time
import serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class SerialPortManager():
    def __init__(self):
        pass

    ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1           
    )
    
    def readMsg(self):
        msg = str(self.ser.readline().strip(), 'utf-8')
        return msg

    def writeMsg(msg):
        ser.write(str.encode(msg))
    
    def isOpen():
        serIsOpen = ser.isOpen()
        return serIsOpen
    
    def close():
        ser.close()
        
        
        
        
        