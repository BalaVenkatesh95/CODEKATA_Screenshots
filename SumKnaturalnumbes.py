def sum_of_k_natural_numbers(K):
    return (K * (K + 1)) // 2
#Formula, K(K+1)/2
K = int(input())
result = sum_of_k_natural_numbers(K)
print(result)
