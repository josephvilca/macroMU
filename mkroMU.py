import win32api
import keyboard
import time

left = win32api.GetKeyState(0x01)
right = win32api.GetKeyState(0x02)
rightButton = win32api.GetKeyState(0x02)
#leftButton = win32api.GetKeyState()

def leftButtonPressed():
	return win32api.GetKeyState(0xA6)  < 0 

def leftButtonReleased():
	return win32api.GetKeyState(0x02)  > 0 


def leftPressed():
	return win32api.GetKeyState(0x01)  < 0 

def leftReleased():
	return win32api.GetKeyState(0x01)  > 0 

def pressQWE():
	keyboard.press_and_release("q")
	time.sleep(0.05)
	keyboard.press_and_release("w")
	time.sleep(0.05)
	keyboard.press_and_release("e")
	time.sleep(0.05)

while True:
	if (leftButtonPressed()):
		print("papi tas presionando click izquierdo")
		pressQWE()


	time.sleep(0.05)