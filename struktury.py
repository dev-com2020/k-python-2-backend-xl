parzyste = [x * 2 for x in range(10) if x % 2 == 0]

# równoważny kod w python
parzyste = []

for x in range(10):
    if x % 2 == 0:
        parzyste.append(x * 2)

print(parzyste)

kwadraty = {x: x**2 for x in range(1, 11)}
print(kwadraty)