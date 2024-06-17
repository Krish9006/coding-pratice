class Solution(object):
    def judgeSquareSum(self, c):
       
        a = 0
        b = int(c ** 0.5)
        
        while a <= b:
            current_sum = a * a + b * b
            if current_sum == c:
                return True
            elif current_sum < c:
                a += 1
            else:
                b -= 1
        
        return False
