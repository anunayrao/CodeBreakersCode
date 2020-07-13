class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        
        
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                profit += prices[i+1] - prices[i]
                
        return profit
        
'''
        Pseuducode:
        1. Iterate over the prices and check if the price at the next day is bigger than current day and if it is then buy the stock and sell it next day. 
        2. Cummulative of all the profit will be the maximum profit as we can do as many transaction as possible.  
        '''