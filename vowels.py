user_input = input()
vowels = 'aeiouAEIOU'


def hasvowels(string):
    for char in user_input[:]:
        if char in vowels:
            return "yes"
        else:
            return "no"

answer = hasvowels(user_input)
print(answer)






