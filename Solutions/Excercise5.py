'''
Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.
'''

N, K = map(int, input().split())
#Elements of N
O, P, Q, R = map(int, input().split())
def K_in_N(O, P, Q, R, K):
    if K == O or K == P or K == Q or K == R:
        return "yes"
    else:
        return "no"

result = K_in_N(O, P, Q, R, K)
print(result)



