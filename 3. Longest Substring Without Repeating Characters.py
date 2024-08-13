class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        result = 0
        for x in range(len(s)):  # loop through the string
            while (
                s[x] in charSet
            ):  # keep removing the other side of the window until reaches dupe, so that substring is a continous one
                charSet.remove(s[l])
                l += 1
            charSet.add(s[x])
            result = max(result, x - l + 1)
        return result
