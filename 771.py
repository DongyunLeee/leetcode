class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        Hash = {}
        for char in jewels:
            if char in Hash:
                Hash[char] = 1
            else:
                Hash[char] += 1

        ret = 0
        for i, j in Hash:
            if i in jewels:
                ret += j

        return ret