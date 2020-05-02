class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        c = 0
        JewelSet = set(J)
        for i  in  S:
            if i in JewelSet:
                c+=1
        return c