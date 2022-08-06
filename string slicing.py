# greeting = "Good Morning, "
# name = "harsh"
# print(type(name))

# Concatenating two strings
# c = greeting + name
# print(c)
name = "harsh"
# print(name[4])
# name[3] = "d" --> Does not work

# print(name[1:4])
# print(name[:4]) # is same as name[0:4]
# print(name[1:]) # is same as name[1:5]
# c = name[-4:-1] # is same is name[1:4]
# print(c)

name = "HarshIsGood"
# d = name[0::3]
d = name [:0:-1]    # very left : start from start.....,,thn 2nd : : skip that(in this 0 position),, last : : till -1(last)
print(d)

# why is it printing backwards lol.... because of that [.....line 20]