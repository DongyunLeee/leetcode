class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(item in jewels for item in stones)