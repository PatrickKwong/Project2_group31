#!/usr/bin/python
#Cas Donoghue
#Patrick Kwong
#Nicholas Vrontakis
#Project 2 CS325

# cents = change amount in cents, coins = increasing array of coin values
def get_change(coins, cents):
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
