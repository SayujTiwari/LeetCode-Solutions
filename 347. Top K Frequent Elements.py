class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashMap = {}
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)
        # sort the map from highest to lowest frequency
        sortedOne = list(
            sorted(hashMap.items(), key=lambda item: item[1], reverse=True)
        )
        output = []
        # looping to output correct amount
        for i in range(k):
            output.append(sortedOne[i][0])
        return output
