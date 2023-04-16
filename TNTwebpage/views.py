from django.shortcuts import render
from django.http import HttpResponse


from pyfirmata import Arduino, SERVO, util
from time import sleep


#Create your views here.
def moveFinger(pin, angle):
    for i in range(0, angle):
        board.digital[pin].write(i)
        sleep(0.005)
    for i in range(angle, 0, -1):
        board.digital[pin].write(i)
        sleep(0.005)


port = 'COM3'
board = Arduino(port)

servo0 = 5  # Index
servo1 = 6  # Middle
servo2 = 10  # Ring
servo3 = 9  # Pinky
# servo4 = 6 #Pinkie
# servo5 = 7 #Wrist


board.digital[servo0].mode = SERVO
board.digital[servo1].mode = SERVO
board.digital[servo2].mode = SERVO
board.digital[servo3].mode = SERVO


# board.digital[servo4].mode = SERVO
# board.digital[servo5].mode = SERVO






def home(request):
    return render(request, "index.html")


def testarm(request):
    return render(request, "testarm.html")

def index(request):
    moveFinger(servo0, 180)
    #moveFinger(servo_num,90)
    print(servo0)
    return render(request, "testarm.html")


def middle(request):
    moveFinger(servo1, 180)
   # moveFinger(servo_num,90)
    print(servo1)
    return render(request, "testarm.html")

def ring(request):
    moveFinger(servo2, 180)
   # moveFinger(servo_num,90)
    print(servo2)
    return render(request, "testarm.html")

def pinky(request):
    moveFinger(servo3, 180)
    #moveFinger(servo_num,90)
    print(servo3)
    return render(request, "testarm.html")