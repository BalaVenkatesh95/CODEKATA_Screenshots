N, M = map(int, input().split())
result = 0
if N > 0 or M > 0:
    # Extract the rightmost digits of a and b
    digit_N = N % 10
    digit_M = M % 10
    # Add the digits without considering carry
    sum_without_carry = (digit_N + digit_M) % 10

    print(sum_without_carry)