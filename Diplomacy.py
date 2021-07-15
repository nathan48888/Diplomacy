# Diplomacy.py

import sys

def diplomacy_solve():
	
	action_list = ["Move", "Support", "Hold"]
	input_list = []

	while True:

		line = sys.stdin.readline()
		a = line.split()
		
		# break loop after final line
		if len(a) < 3:	
			break
		
		else:
		
			assert len(a[0]) == 1
			assert len(a[1]) > 0
			assert a[2] in action_list

			input_list.append(a)

	test = diplomacy_eval(input_list)

	return diplomacy_print(test)


def diplomacy_eval(a):
	
	# dict follows this format: {City: {Army: {num_supports}}}
	cities_dict = {}

	for entry in a:
		cities_dict[entry[1]] = {}

	for entry in a:
		action = entry[2]

		# army in city or origin for "Hold" and "Support"
		if action == "Hold":
			cities_dict[entry[1]][entry[0]] = [0]
		
		if action == "Support":
			cities_dict[entry[1]][entry[0]] = [0]
		
		# army in city following action for "Move"
		if action == "Move":
			cities_dict[entry[3]][entry[0]] = [0]

	for entry in a:
		action = entry[2]

		if action == "Support":
			army = entry[3]

			for i in cities_dict:
				for j in cities_dict[i]:

					# increment number of supports for each army with supports
					if j == army:
						cities_dict[i][army][0] += 1

	output_dict = {}

	for key in cities_dict:
		
		# if only one army in city, that army survives
		if len(cities_dict[key]) == 1:
			temp_safe_list = list(cities_dict[key])
			output_dict[temp_safe_list[0]] = key

		# if > 1 army in city, army with most supports survives (or none survive)
		elif len(cities_dict[key]) > 1:
			temp_army_list = []
			temp_support_list = []

			for army in cities_dict[key]:
				temp_support_list.append(cities_dict[key][army][0])
				temp_army_list.append(army)
			
			copy_temp_support_list = temp_support_list.copy()		
			max_key_1 = max(copy_temp_support_list)
			copy_temp_support_list.remove(max_key_1)
			max_key_2 = max(copy_temp_support_list)
			
			# if most supports and second most supports are equal, city has no survivors
			if max_key_1 == max_key_2:

				for i in temp_army_list:
					output_dict[i] = "[dead]"

			# if only one army with most supports, that army survives
			else:
				position = temp_support_list.index(max(temp_support_list))
				output_dict[temp_army_list[position]] = key
				temp_army_list.pop(position)

				for i in temp_army_list:
					output_dict[i] = "[dead]"

	return output_dict


def diplomacy_print(output_dict):

	sorted_dict = sorted(output_dict)

	for i in sorted_dict:
		print(i, output_dict[i])


if __name__ == '__main__':
	diplomacy_solve()