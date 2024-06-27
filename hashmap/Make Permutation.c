def can_make_permutation(N, A):
    used = set()
    for num in A:
        candidate = num
        while candidate <= N and candidate in used:
            candidate += 1
        if candidate > N:
            return False
        used.add(candidate)
    return True

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    if can_make_permutation(N, A):
        print("YES")
    else:
        print("NO");