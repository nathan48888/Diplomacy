# Diplomacy

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

	for entry in a:
		
		action = entry[2]

		if action == "Hold":

			cities_dict[entry[1]][entry[0]] = [0]
		
		if action == "Support":

			cities_dict[entry[1]][entry[0]] = [0]
		
		if action == "Move":

			cities_dict[entry[3]][entry[0]] = [0]

	for entry in a:

		action = entry[2]

		if action == "Support":

			army = entry[3]

			for i in cities_dict:

				for j in cities_dict[i]:

					if j == army:

						cities_dict[i][army][0] += 1

	war_list = []

	for i in cities_dict:
		
		battle_dict = {}

		for j in cities_dict[i]:

			battle_dict[j] = cities_dict[i][j][0]

		battle_dict_copy = battle_dict.copy()

		if len(battle_dict) > 1:
		
			max_key_1 = max(battle_dict_copy, key=battle_dict_copy.get)
			
			battle_dict_copy.pop(max_key_1)

			max_key_2 = max(battle_dict_copy, key=battle_dict_copy.get)

		battle_dict_copy = battle_dict.copy()

		if max_key_1 == max_key_2:

			for k in battle_dict_copy:

				battle_dict.pop(k)

		else:

			for k in battle_dict_copy:
				
				if k != max_key_1:

					battle_dict.pop(k)
		
		war_list.append(battle_dict)

	return war_list

if __name__ == '__main__':
	diplomacy_read()


'''
def diplomacy_print():
	return

def diplomacy_solve():
	return
'''
