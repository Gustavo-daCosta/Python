total = 0
for c in range(6, 101, 2):
    if c == 6:
        print(c, end='')
    if c >= 8:
        print(f' + {c}', end='')
    total += c
print()
print(f'Total: {total}')