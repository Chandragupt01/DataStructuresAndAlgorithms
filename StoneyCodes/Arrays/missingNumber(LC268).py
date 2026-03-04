class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
            


# Using Summation of all number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summation = sum(nums)
        tSum=0
        for i in range(len(nums)+1):
            tSum=tSum+i

        return tSum-summation
