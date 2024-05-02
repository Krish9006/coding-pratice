class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        set_a=set(word)
        count=0
        for i in set_a:
            if  i.upper() in set_a and i.lower() in set_a:
               count+=1
            
        return counts//2
            
        