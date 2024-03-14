# 1.8Write a Python program to print Fibonacci series upto n terms.
# Program:

def fibonacci_series(num):
    first_term,second_term=0,1
    if(num<=0):
        print("Enter The Positive Numbers !")
    elif(num==1):
        print("Fibonacci Series up to", num, "terms:")
        print(first_term)
    else:
        print("Fibonacci Series up to", num, "terms:")
        print(first_term)
        print(second_term)

        for i in range(2,num):
            next_term=first_term+second_term
            print(next_term)
            first_term=second_term
            second_term=next_term


num = int(input("Enter The Number Of Terms for Fibonacci Series:"))
fibonacci_series(num)
