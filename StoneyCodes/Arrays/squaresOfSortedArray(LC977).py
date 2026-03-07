class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in nums:
            result.append(i*i)
        return sorted(result)

        
#Optimal
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[]
        i=0
        j=len(nums)-1
        while i<=j:
            if abs(nums[i])>abs(nums[j]):
                res.append(nums[i]**2)
                i+=1
            else:
                res.append(nums[j]**2)
                j-=1
        res.reverse()
        return res