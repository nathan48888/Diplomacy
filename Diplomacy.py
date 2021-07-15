# diplomacy

import sys

class Armies():

	def __init__(self, name, city, action, *obj):
		self.name = name
		self.city = city
		self.action = action
		self.obj = obj

	

def diplomacy_read(s):
	
	action_list = ["Move", "Support", "Hold"]

	input_list = []

	while True:

		line = sys.stdin.readline()
		
		if line == "":
			
			break
		
		else:
			
			a = line.split()

			assert len(a[0]) == 1
			assert len(a[1]) > 0
			assert len(a[2]) in action_list

			input_list.append(a)

	return input_list


def diplomacy_eval(a):
	return

def diplomacy_print():
	return

def diplomacy_solve():
	return
