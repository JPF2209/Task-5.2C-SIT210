from tkinter import *  
import tkinter.font
import platform
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Setting up blue LED
bLed = 18
GPIO.setup(bLed, GPIO.OUT)
bPwm = GPIO.PWM(bLed, 50)
bPwm.start(0)

#Setting up red LED
rLed = 23
GPIO.setup(rLed, GPIO.OUT)
rPwm = GPIO.PWM(rLed, 50)
rPwm.start(0)

#Setting up green LED
gLed = 16
GPIO.setup(gLed, GPIO.OUT)
gPwm = GPIO.PWM(gLed, 50)
gPwm.start(0)

#Setup window and font for window
win = Tk()
win.title("LED Setter")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

#Set global variables to work with slider
global blue
global red
global green
blue = False
red = False
green = False

#Function to setting the button light condition
def setCondition(colour):
	global blue
	global red
	global green
	#If blue is pressed
	if colour == "blue":
		blue = True
		green = False
		red = False
		bPwm.ChangeDutyCycle(100)
		rPwm.ChangeDutyCycle(0)
		gPwm.ChangeDutyCycle(0)
	#If red is pressed
	if colour == "red":
		blue = False
		green = False
		red = True
		bPwm.ChangeDutyCycle(0)
		rPwm.ChangeDutyCycle(100)
		gPwm.ChangeDutyCycle(0)
	#If green is pressed
	if colour == "green":
		blue = False
		red = False
		green = True
		bPwm.ChangeDutyCycle(0)
		rPwm.ChangeDutyCycle(0)
		gPwm.ChangeDutyCycle(100)		

#Set blue pwm
def bsetPwm(newvalue):	
	if blue == True:
		bPwmValue.set(newvalue)
		bPwm.ChangeDutyCycle(float(newvalue)) 

#Set red pwm
def rsetPwm(newvalue):	
	if red == True:
		rPwmValue.set(newvalue)
		rPwm.ChangeDutyCycle(float(newvalue)) 
	
#Set green pwm	
def gsetPwm(newvalue):	
	if green == True:
		gPwmValue.set(newvalue)
		gPwm.ChangeDutyCycle(float(newvalue)) 
    
#Program to exit program
def exitProgram():
	GPIO.cleanup()
	win.destroy()

#Setting values for red, blue and green LEDs
bPwmValue = StringVar()
rPwmValue = StringVar()
gPwmValue = StringVar()

#For blue button and slider
blueButton = Button(win, text = 'Turn Blue LED On', font = myFont, command = lambda: setCondition("blue"), bg = 'blue', height = 1, width = 24)
blueButton.grid(row = 1, column = 2)
bSlider = Scale(win, from_=0, to=100, orient=HORIZONTAL, bg = 'blue',command=bsetPwm)
bSlider.grid(row = 1,column = 1)

#For red button and slider
redButton = Button(win, text = 'Turn Red LED On', font = myFont, command = lambda: setCondition("red"), bg = 'red', height = 1, width = 24)
redButton.grid(row = 2, column = 2)
rSlider = Scale(win, from_=0, to=100, orient=HORIZONTAL, bg = 'red', command=bsetPwm)
rSlider.grid(row = 2,column = 1)

#For green button and slider
greenButton = Button(win, text = 'Turn Green LED On', font = myFont, command = lambda: setCondition("green"), bg = 'green', height = 1, width = 24)
greenButton.grid(row = 3, column = 2)
gSlider = Scale(win, from_=0, to=100, orient=HORIZONTAL, bg = 'green', command=bsetPwm)
gSlider.grid(row = 3,column = 1)

#Exit button
exitButton = Button(win, text = 'Exit', font = myFont, command = exitProgram, bg = 'cyan', height = 1, width = 6)
exitButton.grid(row = 5,column = 1)

#Mainloop
mainloop()

