class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictS, dictT = {}, {}
        # using get bc it can return something if the key is not found
        for i in range(len(s)):
            # couting how many times it occurs
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
            dictT[t[i]] = 1 + dictT.get(t[i], 0)
        # compare them to make sure they are equal in letter counts
        for c in dictS:
            if dictS[c] != dictT.get(c, 0):
                return False
        return True


print(Solution().isAnagram("anagram", "nagaram"))
