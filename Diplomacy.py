# diplomacy

import sys


def diplomacy_read():
	
	action_list = ["Move", "Support", "Hold"]

	input_list = []

	while True:

		line = sys.stdin.readline()
	
		a = line.split()
		
		if len(a) < 3:	
			break
		
		else:
			
			a = line.split()

			assert len(a[0]) == 1
			assert len(a[1]) > 0
			assert a[2] in action_list

			input_list.append(a)

	print(input_list)


def diplomacy_eval(a):
	return

def diplomacy_print():
	return

def diplomacy_solve():
	return
