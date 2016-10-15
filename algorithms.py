from math import floor
import random
import time

# Simple Enumeration Maximum Subarray Algorithm
# Takes array as parameter
def enumMaxSub(ls):

        # Check if only one element in array
        if len(ls) == 1:
                return 0,0,ls[0]
        else:
                maxSum = 0
                start = end = 0
                for i in range (0,len(ls)):		
                        for j in range (i+1, len(ls)):
                                sum = 0
                                
                                # add values from i to j
                                for k in range (i,j+1):
                                        sum += ls[k]
                                # check if sum is greater than current max	
                                if sum > maxSum:
                                        maxSum = sum
                                        start = i
                                        end = j
                                
                return start, end, maxSum
	
# Improved Enumeration Maximum Subarray Algorithm
# Takes array as parameter
def betterEnumMaxSub(ls):

        # Check if only one element in array
        if len(ls) == 1:
                return 0,0,ls[0]
        else:
                maxSum = 0
                start = end = 0
                for i in range (0,len(ls)):
                        sum = ls[i]
                        
                        for j in range (i+1, len(ls)):
                                # add new value to sum
                                sum += ls[j]
                                
                                # check if sum is greater than current max
                                if sum > maxSum:
                                        maxSum = sum
                                        start = i
                                        end = j
                                
                return start, end, maxSum

# Calculates maximum crossing subarray
# takes array, low index, mid index, and high index as parameters
def maxCrossSub(ls, low, mid, high):
	
	sumLeft = float("-inf")	
	maxLeft = None
	sum = 0
	for i in range(mid, low-1, -1):
		sum += ls[i]
		if (sum > sumLeft):
			sumLeft = sum
			maxLeft = i
			
	sumRight = float("-inf")	
	maxRight = None
	sum = 0
	for j in range(mid+1, high+1):
		sum += ls[j]
		if (sum > sumRight):
			sumRight = sum
			maxRight = j
	
	return maxLeft, maxRight, sumLeft + sumRight

# Calculates maximum subarray using recursive method	
def maxSubRec(ls, low, high):	
	if (low == high):
		return low, high, ls[low]
	else:
		mid = int(floor((low+high)/2))

		# Calculate left, right, and crossing max subarrays
		leftLow, leftHigh, leftSum = maxSubRec(ls, low, mid)
		rightLow, rightHigh, rightSum = maxSubRec(ls, mid+1, high)
		crossLow, crossHigh, crossSum = maxCrossSub(ls, low, mid, high)

		# Determine overall max and return
		if (leftSum >= rightSum and leftSum >= crossSum):
			return leftLow, leftHigh, leftSum
		elif (rightSum >= leftSum and rightSum >= crossSum):
			return rightLow, rightHigh, rightSum
		else:
			return crossLow, crossHigh, crossSum

# Linear maximum subarray algorithm		
def iterMaxSub(ls):
        
        curSum = maxSum = ls[0]
        i = j = 0          
        start = end = 0  
        for j in range (1, len(ls)):
                curSum += ls[j]
                if ls[j] > curSum:
                        curSum = ls[j]
                        i = j

                if curSum > maxSum:
                        maxSum = curSum
                        start = i 
                        end = j
        return start, end, maxSum  		
	
def loadInput(fileName):

        # Loads arrays from MSS_Problems.txt
        mssProblems = []
        with open(fileName) as file:
                for line in file:
                        if line.strip():
                                data = line.replace('[', '').replace(']','').replace(' ', '')
                                mssProblems.append([int(num) for num in data.split(',') if num not in '\n'])
                
                return mssProblems

def generateArray(numElements):

        randomArray = []
        for i in range(0, numElements+1):
                randomArray.append(random.randrange(-100, 101))
        return randomArray

def runTestProblems():
        # Get arrays from file
        problems = loadInput('MSS_Problems.txt')
        # Create output file for results
        output = open('MSS_Results.txt', 'w+')

        # Finding largest subarray and write to results file
        for i in range (0, len(problems)):
                max = iterMaxSub(problems[i])
                output.write(str(problems[i])+"\n")
                output.write(str(problems[i][max[0]:max[1]+1])+"\n")
                output.write(str(max[2])+"\n\n")

# Run average runtime tests. Outputs results to console and file with algorithm name
def runTests(testValues, algorithm):
        
        testArrays = []
        averageTime = 0
        output = open(algorithm+'.txt', 'w+')
        print("Algorithm = %s \n" % algorithm)
        output.write("Algorithm = %s \n\n" % algorithm)

        # Run each array ten times and get average runtime
        for i in range (0, len(testValues)):
                totalTime = 0
                for k in range (0,11):
                        testArrays.append(generateArray(testValues[i]))
                for j in range (0, len(testArrays)):
                        if algorithm == 'Recursive':
                                
                                startTime = time.clock()
                                (maxSubRec(testArrays[j], 0, len(testArrays[j])-1))
                                totalTime += (time.clock() - startTime)
                        elif algorithm == 'Enumeration':
                                startTime = time.clock()
                                (enumMaxSub(testArrays[j]))
                                totalTime += (time.clock() - startTime)
                        elif algorithm == 'BetterEnumeration':
                                startTime = time.clock()
                                (betterEnumMaxSub(testArrays[j]))
                                totalTime += (time.clock() - startTime)
                        else:
                                startTime = time.clock()
                                (iterMaxSub(testArrays[j]))
                                totalTime += (time.clock() - startTime)
                                
                averageTime = round(totalTime/10, 10)
                print ("Input size = %s, average running time = %s seconds" % (testValues[i], averageTime))
                output.write("Input size = %s, average running time = %s seconds\n" % (testValues[i], averageTime))
        print("\n")

def main():

        # Run algorithm on test problems
        runTestProblems()

        # Values to test each algorithm
        testValuesEnumeration = [10, 20, 30, 40, 50, 100, 200, 300, 400, 500]
        testValuesBetterEnumeration = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        testValuesRecursive = [100, 200, 500, 1000, 2000, 10000, 20000, 50000, 100000, 500000]
        testValuesIterative = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]

        # Run tests
        runTests(testValuesEnumeration, 'Enumeration')
        runTests(testValuesBetterEnumeration, 'BetterEnumeration')
        runTests(testValuesRecursive, 'Recursive')
        runTests(testValuesIterative, 'Iterative')
        

if __name__ == "__main__": main()
