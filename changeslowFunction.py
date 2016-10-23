#!/usr/bin/python
#Group 31
#Cas Donoghue
#Patrick Kwong
#Nicholas Vrontakis
#CS325 Project 2 Algorithm 1: Divide and Conquer Algorithm


# Divide and Conquer Algorithm
# Source: divide and conquer algorithm from provided CS325Project2FA16.pdf 

# input
# array V coin denominations
# value A amount of change we are asked to make
# output
# array C coin denominations count used to make change
# value m minimium number of coins returned to make change


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

# testing function be messing with the main project file and loading problems from the text file.
# array V coin denominations
# value A amount of change we are asked to make
# array C coin denominations count used to make change
# value m minimium number of coins returned to make change

def main():
	V = [1, 3, 7, 26]
	A = 22
	print 'V: ', V 
	print 'A: ', A

	C, m = changeslow(V, A)
	print C
	print m

	V = [1, 2, 5]
	A = 10
	print 'V: ', V 
	print 'A: ', A

	C, m = changeslow(V, A)
	print C
	print m

	V = [1, 2, 5, 10]
	A = 10
	print 'V: ', V 
	print 'A: ', A

	C, m = changeslow(V, A)
	print C
	print m

	# this is slow
	V = [1, 5, 10, 25]
	A = 56
	print 'V: ', V 
	print 'A: ', A

	C, m = changeslow(V, A)
	print C
	print m

	# Testing for correctness

	V = [1, 2, 4, 8]
	A = 15
	print 'V: ', V 
	print 'A: ', A

	C, m = changeslow(V, A)
	print C
	print m

	V = [1, 3, 7, 12]
	A = 29
	print 'V: ', V 
	print 'A: ', A

	C, m = changeslow(V, A)
	print C
	print m

	V = [1, 3, 7, 12]
	A = 31
	print 'V: ', V 
	print 'A: ', A

	C, m = changeslow(V, A)
	print C
	print m


if __name__ == "__main__": main()