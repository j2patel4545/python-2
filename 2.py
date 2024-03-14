# 1.2Write a Python program to construct the following pattern, using nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# Program:


n=5
for i in range(0,n):
    for j in range(i+1):
        print("*", end="")
    print()
for i in range(n):
    for j in range(i,4):
        print("*", end="")
    print()
