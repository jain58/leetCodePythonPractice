
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> str:
        cmaxCount = 0
        cmaxString =''
        queue = []
        n = len(s)
        for j in range(n):
            while s[j] in queue:
                queue.pop(0)
            queue.append(s[j])
            if len(queue) > cmaxCount:
                cmaxCount = len(queue)
                cmaxString = ''.join(queue)
        print(cmaxString)
        #return cmaxCount
        return cmaxString
s= Solution()
inputString = "pwwokew"
x = s.lengthOfLongestSubstring(inputString)
assert x == "woke", "x should be 'woke'"

inputString = "bbbbb"
x = s.lengthOfLongestSubstring(inputString)
assert x == "b", "x should be 'b'"

inputString = "abcabcbb"
x = s.lengthOfLongestSubstring(inputString)
assert x == "abc", "x should be 'abc'"