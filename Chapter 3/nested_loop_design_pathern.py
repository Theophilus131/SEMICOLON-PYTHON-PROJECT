for i in range(1, 11):
    print("*" * i)

print("\n ")
for i in range(10, 0, -1):
    print("*" * i)

print()

for i in range(10, 0, -1):
    for j in range(10 + i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()



print("\n ")
for i in range(10):
    for j in range(i, 10):
        print('', end='')
    for j in range(i + 1):
        print("*", end="")
    print()
