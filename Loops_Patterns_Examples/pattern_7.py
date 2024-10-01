# Output
# 10 9 8 7 6 5 4 3 2 1
# 10 9 8 7 6 5 4 3 2 1
# 10 9 8 7 6 5 4 3 2 1
# 10 9 8 7 6 5 4 3 2 1
# 10 9 8 7 6 5 4 3 2 1
# 10 9 8 7 6 5 4 3 2 1
# 10 9 8 7 6 5 4 3 2 1
# 10 9 8 7 6 5 4 3 2 1
# 10 9 8 7 6 5 4 3 2 1
# 10 9 8 7 6 5 4 3 2 1

n = int(input("Enter the number of rows : "))
for i in range(n):
    for j in range(n,0,-1):
        print(str(j),end=' ')
    print()