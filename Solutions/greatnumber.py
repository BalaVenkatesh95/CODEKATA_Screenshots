n = (input())
j=1
digits = [int(digit) for digit in str(n)]
m=sum(digits)
print("m is:",m)
for digit in digits:
    j = j * digit
    sum_of_m_and_j =str(m + j)
print("J is:",j)
print("sum of m and J:",sum_of_m_and_j)
if n == sum_of_m_and_j:
    print("great")
else:
    print("no")








