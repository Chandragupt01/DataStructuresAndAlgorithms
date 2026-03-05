class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        for i in range(n):
            temp=0
            for j in range(n):
                if nums[j]<nums[i]:
                    temp+=1
            res.append(temp)
        
        return res


# Alternate

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp=sorted(nums)
        d={}
        res=[]
        for i,num in enumerate(temp):
            if num not in d:
                d[num]=i
        for i in nums:
            res.append(d[i])

        return res