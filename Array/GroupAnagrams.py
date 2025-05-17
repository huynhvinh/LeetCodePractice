# Problem: https://neetcode.io/problems/anagram-groups
# Can we do better?
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {} #string -> list
        for s in strs:
            sorted_chars = ''.join(sorted(s))
            if sorted_chars not in hashMap:
                hashMap[sorted_chars] = [s]
            else:
                hashMap[sorted_chars].append(s)
        return list(hashMap.values())
