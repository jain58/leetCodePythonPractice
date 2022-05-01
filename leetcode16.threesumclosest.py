import sys
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        output = sys.maxsize

        for x in range(len(nums)):

            lower = x + 1
            higher = len(nums) - 1

            while higher > lower:
                total = nums[lower] + nums[higher] + nums[x]
                if target == total:
                    return total
                elif target < total:
                    higher = higher - 1
                elif target > total:
                    lower = lower + 1
                if abs(target - total) < abs(target - output):
                    output = total

        return output

s = Solution()
input = [1,-2,-3,2,1,-1,-1,1,0,4,5]
target = -1
result = s.threeSumClosest(input, target)
assert result == -1, "output should be -1"
