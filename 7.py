# 1.7To write a Python program to find first n prime numbers. 
# Program:


def prime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return(0)
    return(1)

N = int(input("Enter the number:"))
i=2
lst=[]
while(1):
    if(prime(i)):
        lst.append(i)
        if(len(lst)==N):
            break
    i+=1

print("Frist "+str(N)+" Prime Number Are :",end="")
print(*lst)
