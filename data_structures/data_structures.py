# 1: convert 1024 to binary and hexadecimal
num = 1024
print(bin(num))
print(hex(num))

# 2: round 5.232323 to two decimal places
print(round(5.232323, 2))

# 3: Check if every letter in the string s is lower case
str3 = "hello how are you Mary, are you feeling okay?"
print(str3.islower())

# 4: How many times does the letter 'w' show up in the string below?
str4 = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(str4.count('w'))

# 5: Find the elements in set1 that are not in set2
# 6: Find all elements that are in either set
set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}
print(set1.difference(set2))
print(set1.intersection(set2))

# 7: Create this dictionary {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension
output_dict = {x: pow(x, 3) for x in range(0, 5)}
print(output_dict)

# 8: Reverse the list list1 = [1,2,3,4]
r_list = [1, 2, 3, 4]
r_list.reverse()
print(r_list)

# 9: Sort the list below
list2 = [3, 4, 2, 5, 1]
print(sorted(list2))
