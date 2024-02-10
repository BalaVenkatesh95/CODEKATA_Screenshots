def isbetween(N, L, R):
    if L <= N <= R:
        return "Yes"
    else:
        return "No"

# Example usage
N = int(input())
#To get 2 inputs in same line using space
L, R = map(int, input().split())


result = isbetween(N, L, R)
print(result)
