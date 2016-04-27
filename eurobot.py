import RPi.GPIO as GPIO
from time import sleep
from time import time
import os
import subprocess

GPIO.setmode(GPIO.BCM)

GPIO.setup(9,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

Motor1 = GPIO.PWM(11, 50)
Motor1.start(0)

Steer = 4

def forward(speed):
  GPIO.output(9,GPIO.HIGH)
  GPIO.output(10,GPIO.LOW)
  Motor1.ChangeDutyCycle(speed)

def backward(speed):
  GPIO.output(9,GPIO.LOW)
  GPIO.output(10,GPIO.HIGH)
  Motor1.ChangeDutyCycle(speed)
  
def left(speed):
  string = "echo 0=+10 > /dev/servoblaster"
  os.system(string)
  sleep(1)
  GPIO.output(9,GPIO.HIGH)
  GPIO.output(10,GPIO.LOW)
  Motor1.ChangeDutyCycle(speed)

def right(speed):
  string = "echo 0=-10 > /dev/servoblaster"
  os.system(string)
  sleep(1)
  GPIO.output(9,GPIO.HIGH)
  GPIO.output(10,GPIO.LOW)
  Motor1.ChangeDutyCycle(speed)

def stop():
  GPIO.output(9,GPIO.LOW)
  GPIO.output(10,GPIO.LOW)
  GPIO.output(11,GPIO.LOW)

def get_range():
  sonar = subprocess.Popen(['./sonar'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
  out, err = sonar.communicate()  
  split_output = out.split('\n')  
  results_list = []  
  split_output.pop()
  for line in split_output:  
	  results_list.append(int(line))  
	  distance = (sum(results_list)/len(results_list))
  return distance

def smart():
  way = "forward"
  string = "echo 0=150 > /dev/servoblaster" #Pan Sensor to center
  os.system(string)
  print "Smart started, pan to center"
  distance = get_range()
  print "Front distance %.1f " % distance
  if distance < 30:
    print "Distance %.1f " % distance
    stop()
    string = "echo 0=110 > /dev/servoblaster" #Pan Sensor to left
    os.system(string)
    sleep(1)
    disleft = get_range()
    print "Left distance %.1f " % disleft
    if disleft < 10:
      string = "echo 0=150 > /dev/servoblaster" #Pan Sensor to center
      os.system(string)
      sleep(1)
      distance = get_range()
      print "Front distance after left turn %.1f" % distance
    else:
      way = "left"
      string = "echo 0=150 > /dev/servoblaster" #Pan Sensor to center
      os.system(string)
      if distance < 1000:
        string = "echo 0=190 > /dev/servoblaster" #Pan Sensor to right
        os.system(string)
        sleep(1)
        disright = get_range()
        print "Right distance %.1f " % disright
        way = "right"
        string = "echo 0=150 > /dev/servoblaster" #Pan Sensor to center
        os.system(string)
        if disright < 1000:
          stop()
        else:
          way = "back"
  else:
    way = "forward"
  return way

while True:
  smart()
  if smart() == "left":
    print "Turn left"
    left(40)
    smart()
    sleep(1)
  if smart() == "right":
    print "Turn right"
    right(40)
    smart()
    sleep(1)
  if smart() == "back":
    backward(40)
    sleep(1)
    smart()
  else:
    forward(80)
    distance = get_range()
    print "Distance %.1f " % distance

  sleep(0.5)

GPIO.cleanup()
