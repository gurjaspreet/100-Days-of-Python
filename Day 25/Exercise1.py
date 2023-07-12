hashtags = ['holiday', 'sport', 'fit', None, 'fashion']

flag = True
for i in hashtags:
    if type(i) != str:
        flag = False
        break
    
print(flag)