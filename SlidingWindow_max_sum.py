import math
from typing import List

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_subarray = -math.inf
#         result = -math.inf
#         for num in nums:
#             tmp_max = max_subarray + num
#             max_subarray = max(tmp_max,num)
#             result = max (result,max_subarray)
#         return result

class Solution:
    def maxsum_subarray(self, K, arr):
      maxWindowSum = 0.0
      windowSum, windowStart = 0.0, 0
      for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]  # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if windowEnd >= K - 1:
          if maxWindowSum <windowSum:
            maxWindowSum = windowSum
          windowSum -= arr[windowStart]  # subtract the element going out
          windowStart += 1  # slide the window ahead

      return maxWindowSum


#Input: [2, 1, 5, 1, 3, 2], k=3
#Output: 9

input= [2, 1, 5, 1, 3, 2]
k=3
s = Solution()
print("Averages of subarrays of size K:")
result = s.maxsum_subarray(k, input)
print("Averages of subarrays of size K: " + str(result))
