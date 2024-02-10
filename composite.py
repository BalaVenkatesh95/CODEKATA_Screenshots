import math
num = int(input())
sqrt_num = int(math.sqrt(num))
for i in range(2, sqrt_num + 1):
    if num % i == 0:
       print("yes")






