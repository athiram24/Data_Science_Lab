n = int(input("Enter a number"))
s=0
for i in range (2,n+1):
    if i%2 == 0:
        s = s + i**3
print("sum =",s)

