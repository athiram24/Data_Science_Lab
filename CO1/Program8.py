# Program to multiply two matrices X and Y transpose

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
r = len(Y)
c = len(Y[0])
# result is 3x4
# result = [[0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0]]
for i in range(r) :
    for j in range(c):
        Y[j][i] = Y[i][j]

for i in range(r):
    for j in range(c):
        print("\t",Y[i][j])
    print("\n")