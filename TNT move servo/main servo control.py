from pyfirmata import Arduino, SERVO, util
from time import sleep

from Variables import l,m,r

def findValue(left_bit, middle_bit, right_bit):
    value= left_bit*(2**2) + middle_bit*(2**1) + right_bit*(2**0)
    return value

def rotateservo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.1)

port = 'COM4'

servo1 = 2 #Thumb
servo2 = 3 #Index 
servo3 = 4 #Middle
servo4 = 5 #Ring
servo5 = 6 #Pinkie
servo6 = 7 #Wrist

board = Arduino(port)

board.digital[servo1].mode = SERVO
board.digital[servo2].mode = SERVO
board.digital[servo3].mode = SERVO
board.digital[servo4].mode = SERVO
board.digital[servo5].mode = SERVO
board.digital[servo6].mode = SERVO

name = findValue(l,m,r)

rotateservo(vars('servo'+name),180)





