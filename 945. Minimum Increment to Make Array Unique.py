class Solution:
    def minIncrementForUnique(self, A):
        A.sort()
        moves = 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                increment = A[i - 1] - A[i] + 1
                A[i] += increment
                moves += increment
        return moves;;


