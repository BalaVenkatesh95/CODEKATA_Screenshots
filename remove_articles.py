def remove_articles(input_sentence):

words = sentence.split()
print(words)
articles = {'The', 'the', 'a', 'A', 'an', 'AN'}
filtered_words = [word for word in words if word.lower() not in articles]
return ' '.join(filtered_words)

input_sentence = input()
result = remove_articles(input_sentence)