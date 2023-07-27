pv = 1000
r = 0.04

i = 1
amt = pv * (1 + r) ** i
while amt < 2 * pv:
    i += 1
    amt = pv * (1 + r) ** i

print(f'Future value: {amt:.2f} USD. Number of periods: {i} years')