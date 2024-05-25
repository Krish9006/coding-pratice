from typing import List

class Solution:
    def reverse(self, stack: List[int]) -> None:
        """
        Do not return anything, modify stack in-place instead.
        """
       
        reversed_stack = []

      
        while stack:
            reversed_stack.append(stack.pop())

       
        for element in reversed_stacks:
            stack.append(element)
        