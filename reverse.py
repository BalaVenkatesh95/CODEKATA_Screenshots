user_input = input()
reversed_string = user_input[::-1]
capitalize_string = reversed_string.capitalize()
print(capitalize_string)
#syntaxfor slicing:sequence[start:stop:step]
#.capitalize() - to start string with capital letter
'''
Where:
start (optional): The starting index of the slice. If not specified, it defaults to 0 (the beginning of the sequence).
stop (optional): The ending index of the slice. If not specified, it defaults to the end of the sequence.
step (optional): The step size used to skip elements in the sequence. If not specified, it defaults to 1.
'''
