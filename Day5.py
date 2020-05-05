class Solution:
    def firstUniqChar(self, s: str) -> int:
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])