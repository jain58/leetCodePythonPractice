import math
from typing import List


class BruteForce_Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)

        return max_subarray


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -math.inf
        result = -math.inf
        for num in nums:
            tmp_max = max_subarray + num
            max_subarray = max(tmp_max,num)
            result = max (result,max_subarray)
        return result

input = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
result = s.maxSubArray(input)
print(result)