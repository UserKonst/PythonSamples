# map()

def square(num):
    return num ** 2


nums = [1, 2, 3, 4, 5]

print(list(map(square, nums)))

# filter()

nums2 = [1, 2, 3, 4, 5, 6]


def is_even(num):
    return num % 2 == 0


print(list(filter(is_even, nums2)))

# lambda

print(list(map(lambda num: num ** 2, nums2)))
