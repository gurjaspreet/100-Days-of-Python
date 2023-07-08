text = 'Python programming'

lst = list(set(text.lower().replace(' ', '')))
lst.sort()

print(lst)