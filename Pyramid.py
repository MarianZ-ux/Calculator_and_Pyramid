# Exercise 2
# Create a pyramid of X's for n number of levels.

# x #for each level focus on the num of spaces to the left of X x xx xxx xxxxx xxxxxxx

for i in range(1,6):
    for j in range(6-i):
        print(" ", end="")
    for j in range(i):
        print("x", end=" ")
    print()