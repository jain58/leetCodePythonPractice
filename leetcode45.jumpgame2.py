from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        i,jump,lastPos,maxPos =0,0,0,0
        while i< N-1:
            maxPos = max(maxPos,i+nums[i])
            if i == lastPos:
                lastPos= maxPos
                jump +=1
            i +=1
        return jump

s = Solution()
nums = [2,3,1,1,4]
result = s.jump(nums)
print(result)