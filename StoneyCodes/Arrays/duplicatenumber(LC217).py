class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        seen=set()
        for i in range(n):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False

# Using Hashmap
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq=dict()
        for i in range(len(nums)):
            if nums[i] in freq :
                return True
            freq[nums[i]]=freq.get(nums[i],0)+1
        return False