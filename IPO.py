from heapq import heappush, heappop

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
   
        projects = sorted(zip(capital, profits))
        
        
        available_projects = []
        index = 0
        n = len(projects)
        
        for _ in range(k):
            
            while index < n and projects[index][0] <= w:
                heappush(available_projects, -projects[index][1]) 
                index += 1
            
            if not available_projects:
                
                break
            
          
            w -= heappop(available_projects)
        
        return w;;


