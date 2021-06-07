from random import randint
rand = randint(1, 6)
print(rand)
for c in range(1, 6):
    if rand == c:
        print(f"You rolled a {rand}")