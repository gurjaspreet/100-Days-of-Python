with open('playway.csv', 'r') as file:
    content = file.read().splitlines()
    
d = {
    'Date': [],
    'Close': []
}

for line in content[1:]:
    temp = line.split(',')
    d['Date'].append(temp[0])
    d['Close'].append(float(temp[-2]))
    
print(d)