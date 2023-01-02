################# Approach 1 #########################
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in (
            word.upper(),
            word.lower(),
            word.capitalize(),
        )


################# Approach 2 #########################
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)

        if len(word) == 1:
            return True

        
        if word[0].isupper() and word[1].isupper():
            for i in range(2, n):
                if not word[i].isupper():
                    return False
      
        else:
            for i in range(1, n):
                if word[i].isupper():
                    return False

  
        return True


################# Approach 3 #########################
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
            
        match1, match2, match3 = True, True, True

        
        for i in range(n):
            if not word[i].isupper():
                match1 = False
                break
        if match1:
            return True

        
        for i in range(n):
            if word[i].isupper():
                match2 = False
                break
        if match2:
            return True

      
        if not word[0].isupper():
            match3 = False
        if match3:
            for i in range(1, n):
                if word[i].isupper():
                    match3 = False
        if match3:
            return True

     
        return False

################# Approach 4 #########################
import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word)