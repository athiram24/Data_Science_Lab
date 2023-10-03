#program to count the uppercase and lower case 
s = input("Enter string:")
uc=0
lc=0
for i in s:
    if(i .isupper()):
        uc = uc+1
    elif (i.islower()):
        lc = lc+1
print("Uppercase count:",uc,"\nLowercase count:",lc)   
