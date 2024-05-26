class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:

        indices = []
        for i, num in enumerate(nums):
            if num == x:
                indices.append(i)

      
        answer = []
        for query in queries:
            if query > len(indices):
                answer.append(-1)
            else:
                answer.append(indices[query - 1])

        return answers