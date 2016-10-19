#!/usr/bin/python
#Cas Donoghue
#Patrick Kwong
#Nicholas Vrontakis
#Project 2 algorithm 4 DP

def changedp(coinValueList,change):
   coinsUsed = [0]*(change+1) #keep track of "new" coin that was just "added" to solution
   minCoins = [0]*(change+1)  #keep track of min num coins for each value
   for i in range(0,change+1): #loop through n. n is change you want to make
      coinCount = i #start with 0 end at n
      newCoin = 1 # assume 1 new coin added
      for a in range(0,len(coinValueList)): # loop through possible coin denominations. 
        if(coinValueList[a] <= i):  # only consider denomiantions that can make the current change 
          if(minCoins[i-coinValueList[a]] + 1 < coinCount): # important! if you can make the change in less than
#                                                            the previous change value plus the lowest denomination
#                                                             then you just add the relevent change and update arrays
            coinCount = minCoins[i - coinValueList[a]] + 1 # this tracks lowest num of coins to get current value of i
            newCoin = coinValueList[a] # this value tracks the denomination that was not the lowest denomination
      minCoins[i] = coinCount #just storing in array to be accessible in main, values explained above
      coinsUsed[i] = newCoin
      
   solutionList = []
   denomIndex = change
   while (denomIndex > 0):
    solutionList.append(coinsUsed[denomIndex])
    denomIndex -= coinsUsed[denomIndex]
  

   return str(solutionList),str(minCoins[change])
   # print "Num coins: " + str(minCoins[change]) # min number of total coins will be last element of min array (n)
   # print "Coins used: " + str(solutionList)  #print solutions