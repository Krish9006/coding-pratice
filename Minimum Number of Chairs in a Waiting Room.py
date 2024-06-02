class Solution:
    def minimumChairs(self, s: str) -> int:
        chairs_need = 0
        current_chairs = 0
        
        for event in s:
            if event == 'E':
                current_chairs += 1
                chairs_need = max(chairs_need, current_chairs)
            else:
                current_chairs -= 2
        
        return chairs_need