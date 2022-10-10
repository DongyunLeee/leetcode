from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, msg):
            if len(msg) == len(digits):
                ret.append(msg)
                return

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1, msg+j)

        if not digits:
            return []

        ret = []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        dfs(0, "")

        return ret