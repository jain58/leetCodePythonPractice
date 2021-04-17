from typing import List


#[0,1,2,4,5,7]
[[0,1,2],[4,5],[7]]
[]
num =1
[[0]]
[[0,1]]
[[0,1,2]]
[[0,2],[4]]
[[0,2],[4,5]]
[[0,2],[4,5],[7]]
class Solution:
    def summaryRanges(self, nums: List[int])->List[str]:
        res=[]
        for num in nums:
            if not res or num != res[-1][-1]+1:
                if res and len(res[-1]) >2:
                    res[-1] = [res[-1][0]] + [res[-1][-1]]
                res.append([num])
            else:
                res[-1].append(num)

        if res and len(res[-1]) >2:
            res[-1] = [res[-1][0]] +[res[-1][-1]]
        #return res
        return ['->'.join(map(str,x))for x in res]

##-----------##
s = Solution()
print(s.summaryRanges([0,1,2,4,5,7]))

res2 = [0,1,2,4,5,7]

print (res2[-1])
print (res2[0])
print (res2[3])

res3 = [[0, 2], [4, 5], [7]]

print(res3[-1][-1])