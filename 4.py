# 1.4Write a Python program to check whether an alphabet is a vowel or consonant.
# Program:


data = input("Enter The Alphabet : ")
my_list=['a','e','i','o','u','A','E','I','O','U']
if data in my_list:
    print(f"Your Alphabet '{data}' is Vowel ")
else:
    print(f"Your Alphabet Is '{data}' Consonant")