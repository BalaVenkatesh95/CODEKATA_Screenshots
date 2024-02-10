from sympy import isprime
L, R = map(int, input().split())
sum = 0
for num in range(R+1):
    if num > 1 and isprime(num):
        sum= sum+1
print(sum)