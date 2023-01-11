"""
File: boggle.py
Name: Elvis
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
# Global Variable (no capital letter)
dictionary = {}

def main():
	"""
	TODO:
	"""
	start = time.time()
	read_dictionary()
	# test model
	# array = ['fycl', 'iomg', 'oril', 'hjhu']
	array = []
	first_row = input("1 row of letters: ")
	array.append(input_check(first_row))
	second_row = input("2 row of letters: ")
	array.append(input_check(second_row))
	third_row = input("3 row of letters: ")
	array.append(input_check(third_row))
	fourth_row = input("4 row of letters: ")
	array.append(input_check(fourth_row))
	find_boggle(array)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def input_check(string):
	""" check the validity of input and processing it to a formatted array
	:param string: input
	:return: array
	"""
	array = ""
	# blank after input is not allowed
	if len(string) != 7:
		raise Exception("invalid input, exceeding word limit")
	count = 0
	for char in string:
		if count % 2 == 1:
			if char != " ":
				raise Exception("invalid input, misplace word")
		else:
			if char == " ":
				raise Exception("invalid input, misplace word")
			array += char
		count += 1
	return array


def find_boggle(array):
	# where to store boggle
	boggle = []
	# vertical
	for i in range(4):
		# horizontal
		for j in range(4):
			find_boggle_helper(array, i, j, "", boggle, [])
	print("There are " + str(len(boggle)) + " words in total.")


def find_boggle_helper(array,  i, j, current_str, result, trace):
	# trace the step that being added
	current_str += array[i][j]
	# trace the coordinate of each step
	trace.append((i, j))
	if len(current_str) >= 4 and current_str not in result:
		# make sure the key in the dictionary first so there will not be an key error
		if current_str[:4] in dictionary.keys() and current_str in dictionary[current_str[:4]]:
			result.append(current_str)
			print('Found "' + current_str + '"')
			# check if the word can be longer
			if has_prefix(current_str):
				neb_list = neighbor_finding(i, j, trace)
				for neb in neb_list:
					find_boggle_helper(array, neb[0], neb[1], current_str, result, trace)
					trace.pop()
	else:
		neb_list = neighbor_finding(i, j, trace)
		for neb in neb_list:
			find_boggle_helper(array, neb[0], neb[1], current_str, result, trace)
			trace.pop()


def neighbor_finding(i, j, trace):
	neb_list = []
	for side_ver in range(i - 1, i + 2):
		if side_ver < 0 or side_ver >= 4:
			continue
		for side_hoz in range(j - 1, j + 2):
			if side_hoz < 0 or side_hoz >= 4:
				continue
			if (side_ver, side_hoz) not in trace:
				neb_list.append((side_ver, side_hoz))
	return neb_list

def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dictionary
	with open(FILE, 'r') as f:
		for line in f:
			if len(line) >= 4:
				line = line.strip()
				key = line[0:4]
				if key in dictionary:
					dictionary[key].append(line)
				else:
					dictionary[key] = [line]
			else:
				pass


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	global dictionary
	if len(sub_s) <= 4:
		for key in dictionary.keys():
			if key.startswith(sub_s):
				return True
		return False
	else:
		for word in dictionary[sub_s[:4]]:
			if word.startswith(sub_s):
				return True
		return False


if __name__ == '__main__':
	main()
