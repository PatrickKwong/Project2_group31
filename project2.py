#!/usr/bin/python
#Cas Donoghue
#Patrick Kwong
#Nicholas Vrontakis
#Project 2 CS325 

# Call the program with one arguement (formatted .txt file) example: >>python change.py Amount.txt
# will print results to [userinput]change.txt in same directory

import sys

from changeslowFunction import changeslow
#from changegreedyFunction import changegreedy
from changedpFunction import changedp

def load_problems(filename):
	problems = []
	f = open(filename, 'r')
    
	while 1:
		try:
			# read coin denominations, save into coins
			coins = f.readline()
			if coins:
				coins = [int(num) for num in coins.replace('[', '')
					.replace(']', '')
					.replace(' ', '')
					.split(',') if num not in '\n']
			else:
				break

			# read amount change to make, save into change
			change = f.readline()
			if change:
				change = change.replace('\n', '')
				change = int(change)
			else:
				break

		except Exception:
			break

		problems.append((coins, change))

	return problems

def main(filename):
	algorithms = {
		'Algorithm changeslow:': changeslow,
#		'Algorithm changegreedy:': changegreedy,
		'Algorithm changedp:': changedp,
	}

	problems = load_problems(filename)
	
	output_file = '{}change.txt'.format(filename.split('.')[0])

	for algorithm_name, algorithm_function in algorithms.items():
		for problem in problems:
			qty, min = algorithm_function(problem[0], problem[1])

			# write results to output_file with name [input filename]change.txt
			with open(output_file, 'a') as f:
				f.write('{0}\n'.format(algorithm_name))
				f.write('{0}\n'.format(qty))
				f.write('{0}\n'.format(min))

if __name__ == "__main__":
	if len(sys.argv) > 1:
		filename = sys.argv[1]
		main(filename)
	else:
		print('Invalid command line arguments')
		exit(1)