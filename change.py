#!/usr/bin/python
# Cas Donoghue
# Patrick Kwong
# Nicholas Vrontakis
# Group 31
# Project 2 CS325

# Call the program with one arguement (formatted .txt file) example: >>python change.py Amount.txt
# will print results to [userinput]change.txt in same directory

# sys for the -i file
import sys
import csv
import time
from changeslowFunction import changeslow
from changedpFunction import changedp
from change_greedy import get_change

output_runtime_data = True
runtime_data = []

#store file input
fileInput = sys.argv[1]
#simple error indicator, should probably just write a main function
error = 0
#tiny bit of input validation
try:
	fi = open(fileInput,"r")
except IOError:
	error = 1
	print('cannot open',fileInput)

# if user managed to specify an existing file, then do the work.
if (error != 1):
	#store very input line as array of arrays
	arrayOfArrays = []

	for line in fi:
		#ignore blank lines
		if line.strip():
			line = line.replace("[","")
			line = line.replace("]","")
			line = line.replace(" ","")
			line = line.replace('\n',"")
			#parsing on comma
			array = [int(x) for x in line.split(",")]
			#make array of arrays for use in all 4 algorithms.
			arrayOfArrays.append(array)
	fi.close()

	fileOutput = fileInput[:len(fileInput)-4] + 'change.txt'
	with open(fileOutput,"w+") as fo:
		for i in range(0,len(arrayOfArrays),2):
                        testcase_runtime_data = []
                        cur_time = time.clock()
			change, numCoins = get_change(arrayOfArrays[i],arrayOfArrays[i+1][0])
                        testcase_runtime_data.append(round(time.clock() - cur_time, 7))
			fo.write("Algorithm changeslow:\n{0}\n{1}\n".format(change, numCoins))
                        cur_time = time.clock()
			change, numCoins = get_change(arrayOfArrays[i],arrayOfArrays[i+1][0])
                        testcase_runtime_data.append(round(time.clock() - cur_time, 7))
			fo.write("Algorithm changegreedy:\n{0}\n{1}\n".format(change, numCoins))
                        cur_time = time.clock()
			change, numCoins = changedp(arrayOfArrays[i],arrayOfArrays[i+1][0])
                        testcase_runtime_data.append(round(time.clock() - cur_time, 7))
			fo.write("Algorithm changedp:\n{0}\n{1}\n".format(change, numCoins))
                        runtime_data.append(testcase_runtime_data)

	print 'results in ' + fileOutput
	print 'branch test'

        if (output_runtime_data):
                with open("runtime_data.csv", "w+") as csv_file:
                        csv_writer = csv.writer(csv_file, delimiter=',')
                        for algo_data in runtime_data:
                                csv_writer.writerow(algo_data)

# #declare an array of denominations prob1
# coinValueList = [1,3,4]
# #call function
# dpMakeChange(coinValueList,11)
# #declare prob 2 denoms
# coinValueList1 = [1,10,25,50]
# #call function
# dpMakeChange(coinValueList1,40)

