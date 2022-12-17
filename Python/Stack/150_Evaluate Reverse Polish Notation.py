class Solution:
    def solve(self, a,b,c):
        if(c=="+"):
            return a + b
        if(c=="-"):
            return (a) - (b)
        if(c=="*"):
            return a * b
        if(c=="/"):
            return int(float(a)/b)
        return -1
        
    
    
    def evalRPN(self, token: List[str]) -> int:
        stack = []
        
        for i in range(len(token)):
            if(token[i]=="+" or token[i]=="-" or token[i]=="*" or token[i]=="/"):
                b = stack.pop()                
                a = stack.pop()
                result = self.solve(a,b,token[i])
                
                stack.append(result)
            else:
                stack.append(int(token[i]))
        
        return stack[-1]



# Solution 2 without Function

def evalRPN(self, token: List[str]) -> int:
        stack = []
        
        for t in token:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                b = stack.pop()                
                a = stack.pop()
                if t=="+":
                    stack.append(a+b)
                elif t=="-":
                    stack.append(a-b)
                if t=="*":
                    stack.append(a*b)
                if t=="/":
                    stack.append(int(float(a)/b))
                
                
        
        return stack.pop()