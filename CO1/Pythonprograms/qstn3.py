#program to replace all the vowels on a text with *
n = input("Enter a text")
for i in n:
    if i in 'AEIOUaeiou':
        n = n.replace(i,"*")
print(n)

# S = input("Enter a string:")
# print("Before replacing :",S)
# # for i in S:
# #     if i in'aeiouAEIOU':
# #         s = S.replace(i,"*")

# # print("The given string is:",s)
# s = S.replace("a","*")
# print("The given string is:",s)
