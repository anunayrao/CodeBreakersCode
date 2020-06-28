class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        '''
        Pseudocode:
        1. Take a stack to evaluate reverse polish notation.
        2. Now iterate over the tokens list and check if its arithematic operator, 
        if it is 
            then pop the two elements convert them to integer and perform that operation and push the result back to the stack
        Else:
            its a number so just push it in the stack
        3. The result is at the top of the stack which is the only element in the stack.
    
        '''
        stack = deque()
        for token in tokens:
            
            
            
            if token not in "+-/*":
                stack.append(token)
                
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if token is "+":
                    r = b+a
                    stack.append(r)
                elif token is "-":
                    r = b-a
                    stack.append(r)
                elif token is "*":
                    r = b*a
                    stack.append(r)
                else:
                    r = int(b/a)
                    stack.append(r)
        return stack.pop()
        
        
        