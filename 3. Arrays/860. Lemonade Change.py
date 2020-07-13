class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        if len(bills) == 0:
            return True
        
        d = defaultdict(int)
        
        for bill in bills:
            
            if bill == 5:
                d[5] += 1
            elif bill == 10:
                d[10] += 1
                if d[5] == 0:
                    return False
                else:
                    d[5] -= 1
            else:
                if d[10] > 0 and d[5] > 0:
                    d[10] -= 1
                    d[5] -= 1
                elif d[5] >= 3:
                    d[5] -= 3
                else:
                    return False
        return True