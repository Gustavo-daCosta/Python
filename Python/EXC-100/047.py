total = 0
for c in range(500, -1, -50):
    if c == 500:
        print(c, end='')
    if c <= 450:
        print(f' + {c}', end='')
    total += c
print()
print(f'Total: {total}')