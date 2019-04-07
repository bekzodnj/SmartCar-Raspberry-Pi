# import time
import threading
from time import sleep

import cv2
from picamera import PiCamera

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32

from gpiozero import DigitalInputDevice, DistanceSensor, Motor

# Motor pin      18  L Back
#               23  L F
#               24  R F
#               25  R B
# motorIn1 = PWMOutputDevice(18)
# motorIn2 = PWMOutputDevice(23)
# motorIn3 = PWMOutputDevice(24)
# motorIn4 = PWMOutputDevice(25)
# IRsensor       12  R
#               16  L
rightIRSensor = DigitalInputDevice(12)
leftIRSensor = DigitalInputDevice(16)

# IR_tracer      8   L
#               7   R
rightIRTracerSensor = DigitalInputDevice(7)
leftIRTracerSensor = DigitalInputDevice(8)

# DisatanceSensor pin   21 T
#                      20 E
distanceSensor = DistanceSensor(21, 20)

# Motors
motor_left = Motor(18, 23)
motor_right = Motor(24, 25)

forwardpin = False

cap = cv2.VideoCapture(0)
i = 0
LEdge = 0
REdge = 0
lineErr = 0
power = 1


def getDistance():
    return distanceSensor.distance


def forward(left=1.0, right=1.0):
    motor_left.forward(left)
    motor_right.forward(right)


def back(left=1.0, right=1.0):
    motor_left.backward(left)
    motor_right.backward(right)


def turnRight(x=1.0, y=1.0):
    motor_left.forward(x)
    motor_right.backward(y)


def turnLeft(back=1.0, forward=1.0):
    motor_left.backward(back)
    motor_right.forward(forward)


def stop():
    motor_left.stop()
    motor_right.stop()


def lIRsensor():
    return rightIRSensor.value


def rIRsensor():
    return leftIRSensor.value


def rIRTracerSensor():
    return rightIRTracerSensor.value


def lIRTracerSensor():
    return leftIRTracerSensor.value


def assignment1():
    def task1():
        forward()
        sleep(5)
        stop()
        sleep(2)
        back()
        sleep(1)
        turnLeft(0, 1)
        sleep(0.9)
        forward()
        sleep(3)
        stop()
        sleep(2)
        turnRight(1, 0)
        sleep(0.9)
        forward()
        sleep(2)
        turnLeft(1, 1)
        sleep(0.55)
        back()
        sleep(2)
        turnRight(1, 0)
        sleep(0.55)
        stop()
    
    def task2():
        while 1:
            sleep(0.02)
            if getDistance() < 0.3:
                stop()
                break
            else:
                forward()

    def task3():
        while 1:
            sleep(0.02)
            if getDistance() < 0.5:
                back()
            else:
                forward()

class assignment2:
    def task1():
        while 1:
            sleep(0.01)
            if (rightIRSensor == 0):
                if (leftIRSensor == 0):
                    forward()
                else:
                    turnLeft()
            elif(leftIRSensor == 0):
                turnRight()
            else:
                stop()
    def task2():
        leftIRTracerSensorPin = False
        rIRTracerSensorPin = False
        def secondetest():
            sleep(0.3)
            while (1):
                if(leftIRTracerSensor == 1):
                    if (rightIRTracerSensor==True ) And (leftIRTracerSensorPin == Ture):
                        stop()
                if (rightIRTracerSensor == 1):
                    if (rightIRTracerSensor == True ) And (leftIRTracerSensorPin == Ture):
                        stop()
        forward(1,1)
        while 1:
            sleep(0.01)
            if(leftIRTracerSensor == 1):
                if (rightIRTracerSensor==True ) And (leftIRTracerSensorPin == Ture):
                    secondetest()
                leftIRTracerSensorPin == True
            if (rightIRTracerSensor = 1):
                if (rightIRTracerSensor == True ) And (leftIRTracerSensorPin == Ture):
                    secondetest()
                rightIRTracerSensorPin == True

    def task3():
        forward(0.5,0.5)
        leftPin = 0.5
        rightPin = 0.5
        crossLinePin = 0
        while 1:
            sleep(0.01)
            
            if(leftIRTracerSensor == 1):
                if leftPin<1 :
                    leftPin = leftPin + 0.1
            elif leftPin > 0.5:
                leftPin = leftPin - 0.1
            else:
                leftPin= 0.5
            
            if(rightIRTracerSensor ==1):
                if rightPin<1 :
                    rightPin = rightPin + 0.1
            elif rightPin > 0.5:
                rightPin = rightPin - 0.1
            else:
                rightPin= 0.5
            
            if(leftIRTracerSensor == 1 And rightIRTracerSensor == 1):
                crossLinePin = crossLinePin + 1
                sleep(0.2)
            if (getDistance < 0.3):
                stop()
                print('object ditected')
            else:
                if(crossLinePin<3):
                    forward(leftPin,rightPin)
                else:
                    stop()
                    break




