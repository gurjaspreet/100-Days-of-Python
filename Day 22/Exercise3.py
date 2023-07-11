probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]

classes = []

for i in probabilities:
    if i < 0.5:
        classes.append(0)
    else:
        classes.append(1)
        
print(classes)