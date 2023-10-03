# Write a program to reverse a number and find the sum of digits. Accept user input
# n = int(input("Enter a number"))
# rev = 0
# while n>0:
   
#     rem = n%10
#     rev = rev*10+ rem
#     n = n//10
# print("reverse of number :",rev)

n = int(input("Enter a number"))
s = str(n)
print("reverse =",s[::-1])


