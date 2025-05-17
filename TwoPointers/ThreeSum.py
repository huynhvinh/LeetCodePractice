# Problem: https://neetcode.io/problems/three-integer-sum

# Note: How to handle duplicates: Compare with the previous element while
# ensuring the j < k condition holds

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate i

            target = 0 - nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                n = nums[j] + nums[k]
                if n == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    # skip duplicates for j and k
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif n < target:
                    j+=1
                else:
                    k-=1
        return res

    
