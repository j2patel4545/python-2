# 1.6Write a Python program to check whether the given no is Armstrong or not using. 
# Program:


num = int(input("Enter The Num : "))
a=str(num)
power=len(a)
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    digit = digit ** power
    sum += digit
    temp = temp//10
    
if sum == num:
    print(f"Your Number '{num}' Is Armstrong")
else:
    print(f"Your Number '{num}' is Not Armstrong")
