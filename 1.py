# 1.Develop programs to understand the control structures of python.
# 1.1Write a Python Program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700.
# Program:
print("Numbers Between 1500 and 2700 That are divisible by 7 and 5 are : ")

num=[]
for a in range(1500,2701):
    if a % 7 == 0 and a % 5 == 0:
        num.append(a)
print(num)