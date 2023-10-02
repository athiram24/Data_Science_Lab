#pgram to count upper case and lower case in a string
n = input("enter a string")
upper= 0
lower= 0
for i in n:
    if i.isupper():
        upper+=1

    else:
        lower+=1
print("Uppercase count",upper)
print("Lowercase count",lower)
