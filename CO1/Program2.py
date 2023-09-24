#program to replace all the vowels on a text with *
n = input("Enter a text")
for i in n:
    if i in 'AEIOUaeiou':
        n = n.replace(i,"*")
print(n)

