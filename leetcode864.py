import collections

from pip._vendor.msgpack.fallback import xrange


class Solution(object):
    def isNStraightHand(self, hand, W):
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for k in xrange(m, m+W):
                v = count[k]
                if not v: return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1

        return True

s=Solution()
hand = [1,2,3,6,2,3,4,7,8]
W = 3
print(s.isNStraightHand(hand,W))