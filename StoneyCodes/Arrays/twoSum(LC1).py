class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return [-1,-1]
    


# one pass Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        freq=dict()
        for i in range(n):
            rem=target-nums[i]
            if rem in freq:
                return [freq[rem],i]
            freq[nums[i]]=i