#!/usr/bin/python
#Cas Donoghue
#Patrick Kwong
#Nicholas Vrontakis
#Project 2 CS325

# cents = change amount in cents, coins = increasing array of coin values
def get_change(cents, coins):
    change = []
    for num in range(len(coins)):
        change.append(0)
    while (cents > 0):
        for num in range(len(coins)-1, 0, -1):
            if (coins[num] <= cents):
                change[num] += 1
                cents -= coins[num]
                break
    return change

coins = [1, 5, 10, 25]
change = get_change(85, coins)
print change
