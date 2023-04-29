def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

num = my_range(1, 5)

print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))


