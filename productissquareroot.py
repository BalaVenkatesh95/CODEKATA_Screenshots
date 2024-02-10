import math
N, M = map(int, input().split())
square = N*M
squareroot = math.isqrt(square)
if squareroot == N and squareroot == M:
    print("yes")
else:
    print("yes")
