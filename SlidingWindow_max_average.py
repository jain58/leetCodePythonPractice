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
    def find_averages_of_subarrays(self, K, arr):
      result = []
      maxWindowSum = 0.0
      windowSum, windowStart = 0.0, 0
      for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]  # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if windowEnd >= K - 1:
          result.append(windowSum / K)  # calculate the average
          if maxWindowSum <windowSum/K:
            maxWindowSum = windowSum/K
          windowSum -= arr[windowStart]  # subtract the element going out
          windowStart += 1  # slide the window ahead

      return result, maxWindowSum


#Input: [2, 1, 5, 1, 3, 2], k=3
#Output: 9

input = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print("Averages of subarrays of size K:")
result = s.find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
print("Averages of subarrays of size K: " + str(result))
print(result)