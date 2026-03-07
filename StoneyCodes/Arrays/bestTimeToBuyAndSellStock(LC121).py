class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxProfit=0
        for i in range(n):
            for j in range(i+1,n):
                if prices[j]-prices[i]>maxProfit:
                    maxProfit=prices[j]-prices[i]

        return maxProfit
    

# OnePass Solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro=0
        minPrice=prices[0]
        for i in range(len(prices)):
            currentProfit=prices[i]-minPrice
            minPrice=min(prices[i],minPrice)
            maxPro=max(currentProfit,maxPro)

        return maxPro