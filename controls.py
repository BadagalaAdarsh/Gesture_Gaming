from pynput.keyboard import Key, Controller

keyboard = Controller()

global key 
key = None

def donothing():
	global key
	if key == 'a' or key == 's' or key == 'w' or key == 'd':
		keyboard.release(key)
		
		
def left(angle):
	global key
	
	if key == 's' or key == 'w' or key == 'd':
		keyboard.release(key)
		
	bearing=16834-int((angle/90)*16384) 
	'''key = 'w'
	keyboard.press(key)'''
	key = 'a'
	keyboard.press(key)
	
	


def reCentre():
	global key
	if key == 'a' or key == 's' or key == 'd':
		keyboard.release(key)
	key = 'w'
	keyboard.press(key)
	
	
	
def right(angle):
	bearing=16834-int((angle/90)*16384) 
	'''key = 'w'
	keyboard.press(key)'''
	global key
	if key == 'a' or key == 's' or key == 'w':
		keyboard.release(key)
	key ='d'
	keyboard.press(key)
	
	
	
def Brake():
	global key
	if key == 'a' or key == 'w' or key == 'd':
		keyboard.release(key)
	
	key = 's'
	keyboard.press(key)
	
	
