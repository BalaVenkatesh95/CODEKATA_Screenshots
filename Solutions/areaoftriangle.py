import sys
B, H = map(int, input().split())
blen = sys.getsizeof(B)
hlen = sys.getsizeof(H)
if blen <= 1000000 and hlen <= 1000000:
    area = 0.5 * B * H
    print(int(area))

