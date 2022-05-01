import collections

s = "manas"
result = True
count = collections.Counter(s)
chance = 1
for char in count:
   if count[char]%2 != 0:
      chance -= 1
      if chance < 0:
          result = False
          break

print("Result "+str(result))

"""class Solution(object):
    def canPermutePalindrome(self, s):
       
        :type s: str
        :rtype: bool
     
        count = collections.Counter(s)
        chance = 1
        for char in count:
            if count[char]%2 != 0:
                chance -= 1
                if chance < 0:
                    return False
        return True
"""