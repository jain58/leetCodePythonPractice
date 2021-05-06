from collections import defaultdict
from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.prefixSet = defaultdict(set)
        self.suffixSet = defaultdict(set)
        visited = set()
        for i in range(len(words) - 1, -1, -1):
            if words[i] in visited:
                continue
            visited.add(words[i])
            for j in range(len(words[i]) + 1):
                self.prefixSet[words[i][:j]].add(i)
                self.suffixSet[words[i][j:]].add(i)

    def f(self, prefix: str, suffix: str) -> int:
        i = self.prefixSet[prefix]
        j = self.suffixSet[suffix]
        overlap = i & j
        if not overlap:
            return -1
        return max(overlap)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)