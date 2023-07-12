number = 13

prime = True
for i in range(2, number):
    if number % i == 0:
        prime = False
        break
    
if prime:
    print(number, '- prime number')
else:
    print(number, '- not a prime number')