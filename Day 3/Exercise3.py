a, b, c = 1, 5, 4

delta = b ** 2 - 4 * a * c

x1 = (-1 * b - delta ** 0.5) / (2 * a)
x2 = (-1 * b + delta ** 0.5) / (2 * a)

print(f'x1 = {x1:.1f}\nx2 = {x2:.1f}')