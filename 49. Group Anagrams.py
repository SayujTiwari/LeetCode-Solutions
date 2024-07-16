class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        n = len(strs)
        hashMap = {}
        for i in range(n):
            # sorted anagrams by alphabetical order will be indentical, so just group them as list in map then return
            sortedWord = "".join(sorted(strs[i]))
            hashMap[sortedWord] = [strs[i]] + hashMap.get(sortedWord, [])
        return list(hashMap.values())
