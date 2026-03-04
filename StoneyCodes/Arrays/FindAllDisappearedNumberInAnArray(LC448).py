class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        numSet=set(nums)
        result=[]
        for i in range(1,n+1):
            if i not in numSet:
                result.append(i)
        return result
    
# Using HashMap

class Solution(object):
    def findDisappearedNumbers(self, nums):
        res=[]
        n=len(nums)
        freqMap={i:0 for i in range(1,n+1)}
        for num in nums:
            freqMap[num]+=1
        for k,v in freqMap.items():
            if v==0:
                res.append(k)
        return res