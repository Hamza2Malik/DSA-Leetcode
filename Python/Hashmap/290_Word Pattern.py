class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sp = s.split()
        ans = {}
        
        
        if len(sp) != len(pattern) or len(set(pattern)) != len(set(sp)):
            return False
        for i,c in enumerate(pattern):
            if c in ans:
                if ans[c] != sp[i]:
                    return False
                
            else:
                ans[c] = sp[i]
                
        return True