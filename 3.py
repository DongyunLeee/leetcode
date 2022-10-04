class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        arr = []
        for item in s:
            # 문자가 중복되지 않으면 배열에 추가하고 길이 비교
            if item not in arr:
                arr.append(item)
                if ret < len(arr):
                    ret = len(arr)

            # 문자가 중복된 경우, 해당 문자까지 배열에서 제거하고 문자를 배열에 추가함
            else:
                arr = arr[arr.index(item) + 1:]
                arr.append(item)

        return ret