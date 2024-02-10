user_input = input()
sum = 0
if user_input[0]  in {'a', 'A'}:
    sum = sum + 1
if user_input[1]  in {'m', 'M'}:
    sum = sum + 1
if user_input[2]  in {'z', 'Z'}:
    sum = sum + 1
if sum == 3:
    print(1)
else:
    print(0)