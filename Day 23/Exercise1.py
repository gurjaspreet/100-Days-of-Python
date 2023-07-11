items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
items_set = set(items)

hist = {i: items.count(i) for i in items_set}
print(hist)