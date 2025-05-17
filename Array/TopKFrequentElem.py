# Problem: https://neetcode.io/problems/top-k-elements-in-list
# make use of default dict/ counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1
        sorted_elems = sorted(hashMap.items(), key=lambda x: x[1], reverse = True)
        res = []
        for j in range(k):
            res.append(sorted_elems[j][0])
        return res
        
