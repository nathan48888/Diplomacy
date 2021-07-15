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

	test = diplomacy_eval(input_list)
	print(test)


def diplomacy_eval(a):
	
	cities_dict = {}

	for entry in a:
		
		cities_dict[entry[1]] = {}

		if len(entry) == 3:

			cities_dict[entry[1]][entry[0]] = [0]

	
	for entry in a:

		action = entry[2]

		if action == "Support":

			cities_dict[entry[1]][entry[0]] = [0]

			
	




	return cities_dict

if __name__ == '__main__':
	diplomacy_read()


'''
def diplomacy_print():
	return

def diplomacy_solve():
	return
'''
