# Problem: https://neetcode.io/problems/products-of-array-discluding-self
# can we not use hashL and hashR as 2 separate lists?
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodL, prodR = 1, 1
        hashL, hashR = [], []
        for i in range(len(nums)):
            if i != 0:
                prodL *= nums[i - 1]
            hashL.append(prodL)

        for i in range(len(nums)-1, -1, -1):
            print(i)
            if i != len(nums)-1:
                prodR *= nums[i + 1]
            hashR.append(prodR)
        hashR = hashR[::-1]
        print(hashL)
        print(hashR)
        res = []
        for i in range(len(hashL)):
            res.append(hashL[i] * hashR[i])
        return res
