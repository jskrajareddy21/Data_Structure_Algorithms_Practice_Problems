# Output
#     1
#    121
#   12321
#  1234321
# 123454321

n = int(input("Enter the number of rows : "))

for i in range(1,n+1):
    print(' '*(n-i), end='')

    for j in range(1, i+1):
        print(j,end='')

    for k in range(i-1,0,-1):
        print(k,end='')
    print()