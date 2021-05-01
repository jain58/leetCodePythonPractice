from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visitedSet = []
        result = []
        # print(nums)
        for x in range(len(nums) - 1):
            lower = x + 1
            higher = len(nums) - 1
            target = 0 - nums[x]

            while higher > lower:
                total = nums[lower] + nums[higher]
                if total == target:
                    currentSet = set([nums[x], nums[lower], nums[higher]])
                    if currentSet not in visitedSet:
                        # print (currentSet)
                        visitedSet.append(currentSet)
                        result.append([nums[x], nums[lower], nums[higher]])
                        # print (visitedSet)
                        # print (result)
                    lower = lower + 1
                    higher = higher - 1

                elif total > target:
                    higher = higher - 1

                elif total < target:
                    lower = lower + 1

        return result