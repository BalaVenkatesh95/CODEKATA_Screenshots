
input_data = input()
vowels = "AEIOUaeiou"
result = ""
for char in input_data[:]:
    if char not in vowels:
        result = result+char
print(result)