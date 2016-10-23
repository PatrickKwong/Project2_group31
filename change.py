#!/usr/bin/python
#Cas Donoghue
#Patrick Kwong
#Nicholas Vrontakis
#Project 2 CS325

# Call the program with one arguement (formatted .txt file) example: >>python change.py Amount.txt
# will print results to [userinput]change.txt in same directory

# sys for the -i file
import sys
from changedpFunction import changedp
from change_greedy import get_change

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
		        change, numCoins = get_change(arrayOfArrays[i],arrayOfArrays[i+1][0])
		        fo.write("Greedy Approach\n{0}\n{1}\n".format(change, numCoins))
		        change, numCoins = changedp(arrayOfArrays[i],arrayOfArrays[i+1][0])
		        fo.write("Dynamic Programming Approach\n{0}\n{1}\n".format(change, numCoins))

	print 'results in ' + fileOutput
	print 'branch test'


# #declare an array of denominations prob1
# coinValueList = [1,3,4]
# #call function
# dpMakeChange(coinValueList,11)
# #declare prob 2 denoms
# coinValueList1 = [1,10,25,50]
# #call function
# dpMakeChange(coinValueList1,40)

