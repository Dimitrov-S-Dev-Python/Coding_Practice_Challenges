n = int(input())

k = n

for row in range(n):
    k -= 1
    for space in range(k):
        print(" ", end="")

    for star in range(0, row + 1):
        print("*", end=" ")

    for space in range(k):
        print(" ", end="")
    print()
