# Output
# 10 9 8 7 6 5 4 3 2 1
# 10 9 8 7 6 5 4 3 2
# 10 9 8 7 6 5 4 3
# 10 9 8 7 6 5 4
# 10 9 8 7 6 5
# 10 9 8 7 6
# 10 9 8 7
# 10 9 8
# 10 9
# 10

n = int(input("Enter the number of rows : "))
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(n-j+1, end=' ')
    print()