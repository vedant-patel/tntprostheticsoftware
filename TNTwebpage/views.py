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

<<<<<<< HEAD
servo0 = 9  # Thumb
servo1 = 10  # Index
servo2 = 6  # Middle
servo3 = 11  # Ring
# servo4 = 6 #Pinkie
# servo5 = 7 #Wrist

=======
servo0 = 5  # Index
servo1 = 6  # Middle
servo2 = 10  # Ring
servo3 = 9  # Pinky
# servo4 = 6 #Pinkie
# servo5 = 7 #Wrist


>>>>>>> test
board.digital[servo0].mode = SERVO
board.digital[servo1].mode = SERVO
board.digital[servo2].mode = SERVO
board.digital[servo3].mode = SERVO


# board.digital[servo4].mode = SERVO
# board.digital[servo5].mode = SERVO


<<<<<<< HEAD
def index(request):
=======




def home(request):
>>>>>>> test
    return render(request, "index.html")


def testarm(request):
<<<<<<< HEAD
    servo_num = 0
    print(servo_num)
    return render(request, "testarm.html")


def testarm1(request):
    servo_num = 1
    print(servo_num)
    return render(request, "testarm.html")
=======
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
>>>>>>> test
