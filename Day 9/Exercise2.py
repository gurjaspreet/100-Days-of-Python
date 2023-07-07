text = 'Programming in python.'

vowels = {'a', 'e', 'i', 'o', 'u'}

text = text.lower()
text = text.replace(' ', '')
text = text.replace('.', '')
s = set(text)
s = s.difference(vowels)

print('Number of items:', len(s))