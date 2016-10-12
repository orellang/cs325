from math import floor

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
	
		
		
	
def main():
	list1 = [2]
	max = betterEnumMaxSub(list1)
	print (max)

if __name__ == "__main__": main()
