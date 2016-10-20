""" Function which takes in an array of coin values and a value to make change
for and returns an array with the minimum number of each coin denomination
needed to make change for the amount.

Input: array of coin values, integer for change amount
Output: array of coin numbers corresponding to array of coin values."""

def changeslow(values, amount):

    # Array to hold coins used
    coins = [0]*len(values)

    # Check if single coin equals amount
    for i in range(len(values)):
        if values[i] == amount:
            coins[i] += 1
            return coins, 1

    lowestCount = float("inf")

    # Try all combinations of coins
    for i in range(len(values)):
        if values[i] < amount:
            currentCoins, currentCount = changeslow(values, (amount-(values[i])))

            if currentCount < lowestCount:
                lowestCount = currentCount + 1
                currentCoins[i] += 1
                for j in range(len(coins)):
                    coins[j] = currentCoins[j]

    return coins, lowestCount

""" Function which takes in an array of coin values and a value to make change
for and returns an array with the minimum number of each coin denomination
needed to make change for the amount. Uses greedy principle.

Input: array of coin values, integer for change amount
Output: array of coin numbers corresponding to array of coin values."""
def changegreedy(values, amount):

    k = amount
    coins = [0]*len(values)
    coinCount = 0
    # Keep trying biggest coin possible until k == 0
    for i in range(len(values)-1,-1,-1):
        while (values[i] <= k):
            coins[i] += 1
            coinCount += 1
            k -= values[i]

    return coins, coinCount

""" Function which takes in an array of coin values and a value to make change
for and returns an array with the minimum number of each coin denomination
needed to make change for the amount. Uses dynamic programming.

Input: array of coin values, integer for change amount
Output: array of coin numbers corresponding to array of coin values."""
def changedp(values, amount):

    # Array s to track minimum coins and quantity of each coin used
    minimumCoins = [0]*(amount+1)
    coinsUsed = [0]*(amount+1)

    # Array holding number of each coin used to get amount
    coins = [0]*len(values)

    for i in range(amount+1):
        if i == 0:
            coinUsed = 0
        else:
            coinUsed = 1

        coinsNeeded = i

        # Get value for each amount, checking if already calculated
        for value in values:
            if value <= i:
                if (1+ minimumCoins[i-value]) < coinsNeeded:
                    coinsNeeded = 1 + (minimumCoins[i-value])
                    coinUsed = value
        minimumCoins[i] = coinsNeeded
        coinsUsed[i] = coinUsed

    total = amount

    # Get coins used
    while total > 0:
        coinUsed = coinsUsed[total]
        coins[values.index(coinUsed)] += 1
        total -= coinUsed

    return coins, minimumCoins[amount]

if __name__ == '__main__':

    for i in range(2010, 2205, 5):
        #print(changeslow([1,5,10,25,50], 31)
        print(i)
        print(changegreedy([1,5,10,25,50],i))
        print(changedp([1,5,10,25,50],i))


    

 
