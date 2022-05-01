

class Solutions:
    def maxsumSubArray(self, k, arr):
        windowstart =0
        windowend =0
        windowsum=0
        lengthofwindw=3
        maxsumSubArray =0
        i=0
        while i<k:
            windowsum += arr[i]
            i = i+1
        maxsumSubArray = windowsum
        for windowend in range (k,len(arr)):
            windowstart = windowend-k
            windowsum = windowsum - arr[windowstart]+arr[windowend]
            if maxsumSubArray<windowsum:
                maxsumSubArray = windowsum
        return maxsumSubArray


#
#Input: [2, 1, 5, 1, 3, 2], k=3
#Output: 9

#Input: [2, 3, 4, 1, 5], k=2
#Output: 7

input = [2, 3, 4, 1, 5]
s= Solutions()
result = s.maxsumSubArray(2,input)
print(result)