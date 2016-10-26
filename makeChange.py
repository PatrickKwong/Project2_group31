#!/usr/bin/python
# Cas Donoghue
# Patrick Kwong
# Nicholas Vrontakis
# Group 31
# Project 2 CS325

# Call the program with one arguement (formatted .txt file) example: >>python change.py Amount.txt
# will print results to [userinput]change.txt in same directory

#access info: sys is for file specifications, csv for pretty data output, time for testing
import sys
import csv
import time

############################################## FUNCTION DEFINITIONS#########################################

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# Divide and Conquer Algorithm
# Source: divide and conquer algorithm from provided CS325Project2FA16.pdf 

# input
# array V:coin denominations
# value A: amount of change we are asked to make
# output
# array C: coin denominations count used to make change
# value m: minimium number of coins returned to make change
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def changeslow(V, A):
	# keep track of coins used
	C = [0] * len(V)

	# set the minimum to maximum possible amount (amount ask to make change for, in case we only can use pennies)
	m = A

	# if there is a A-cent coin, then that one coin is the minimum.
	if A in V:
		C[V.index(A)] += 1
		return C, 1

	else: 
		for i in range(0, len(V)):
			if(V[i] <= A):
				C_temp, m_temp = changeslow(V, A - V[i])
				C_temp[i] += 1
				m_temp += 1

				# check if the new m_temp is smaller existing m, if so record the new C and m
				if m > m_temp:
					C = C_temp
					m = m_temp
		return C, m


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# Greedy choice algorithm
# Source: greedy algorithm from provided CS325Project2FA16.pdf 

# input
# array coins: coin denominations
# value cents: amount of change we are asked to make
# output
# array num_coins: coin denominations count used to make change
# value change: minimium number of coins returned to make change
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def changegreedy(coins, cents):
    change = []
    num_coins = 0
    for num in range(len(coins)):
        change.append(0)
    while (cents > 0):
        for num in range(len(coins)-1, -1, -1):
            if (coins[num] <= cents):
                change[num] += 1
                num_coins += 1
                cents -= coins[num]
                break
    return change, num_coins

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# Greedy algorithm
# Source: dp solution from provided CS325Project2FA16.pdf,
# Based on simple min coins approach, added in matrix to store output arrays

# input
# array coinValueList: coin denominations
# value change: amount of change we are asked to make
# output
# array solutionMatrix[change]: coin denominations count used to make change
# value inCoins[change]: minimium number of coins returned to make change
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#
def changedp(coinValueList,change):

	#initialize table elements to store optimal solutions. NOTE: only need table of n = change size 
	initilizeArray = [0]*len(coinValueList) #initialize array to hold solutions (by index)
	solutionMatrix = [initilizeArray]#this is solutions matrix that stores # of each coin by index of coinValueList
	coinsUsed = [0]*(change+1) # array of "new" coin added to obtain optimal solution at each point 0 thru change
	minCoins = [0]*(change+1) # array of num coins used in each optimal solution at each point 0 thru change


	for i in range(1,change+1): # build table for every optimal solution 0 thru change

		index = 0  #used to look up index of desired optimal solutions
		coinCount = i  #initialize to i (the case where solution is change or all 1s)
		newCoin = 0 # initialize to adding the 1 value (coinValueList[0])

		for a in range(0,len(coinValueList)): #loop through all coin value list 
			if(coinValueList[a] <= i): #if less than the current value (do not consider coins greater than current change to make)
				#because coinValueList is sorted in increasing order loop ends on optimal solution for each variable below
				if(minCoins[i-coinValueList[a]] + 1 <= coinCount): # check each value at index i - each coin list value to see if adding that coin is optimal
					coinCount = minCoins[i - coinValueList[a]] + 1 # optimal value for i value of change
					newCoin = a #store index on new coin added
					index = i - coinValueList[a] #store index of the i - coinValueList value that solution came from

		minCoins[i] = coinCount #store min coins at change i
		coinsUsed[i] = newCoin #store new coin added (from index of coinValueList)
		
		#build solution matrix by tracking the index values that make up optimal solutions and addind the new coin.
		temp = []
		for x in range(0,len(solutionMatrix[index])):
			temp.append(solutionMatrix[index][x])
		temp[newCoin] += 1
		solutionMatrix.append(temp)
		
	return solutionMatrix[change],minCoins[change] # return index counts corresponding to coinValueLIst, min coins used in solution

##############################################END FUNCTION DEFINITIONS #########################################



############################################### DRIVER CODE ###################################################

#testing variables, select true for output_runtime_data, false for no test
output_runtime_data = True
runtime_data = []

#Get file specified in execution, parse it and store data in array of arrays 
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

# format file output (solutions) and optional testing data 
	fileOutput = fileInput[:len(fileInput)-4] + 'change.txt'
	with open(fileOutput,"w+") as fo:
		for i in range(0,len(arrayOfArrays),2):
                        testcase_runtime_data = []
                        cur_time = time.clock()
			change, numCoins = changeslow(arrayOfArrays[i],arrayOfArrays[i+1][0])
                        testcase_runtime_data.append(round(time.clock() - cur_time, 7))
			fo.write("Algorithm changeslow:\n{0}\n{1}\n".format(change, numCoins))
                        cur_time = time.clock()
			change, numCoins = changegreedy(arrayOfArrays[i],arrayOfArrays[i+1][0])
                        testcase_runtime_data.append(round(time.clock() - cur_time, 7))
			fo.write("Algorithm changegreedy:\n{0}\n{1}\n".format(change, numCoins))
                        cur_time = time.clock()
			change, numCoins = changedp(arrayOfArrays[i],arrayOfArrays[i+1][0])
                        testcase_runtime_data.append(round(time.clock() - cur_time, 7))
			fo.write("Algorithm changedp:\n{0}\n{1}\n".format(change, numCoins))
                        runtime_data.append(testcase_runtime_data)

	print "Processing..."
	print 'Results saved to ' + fileOutput


        if (output_runtime_data):
        	print 'Runtime data saved to runtime_data.csv:'
                with open("runtime_data.csv", "w+") as csv_file:
                        csv_writer = csv.writer(csv_file, delimiter=',')
                        for algo_data in runtime_data:
                                csv_writer.writerow(algo_data)



