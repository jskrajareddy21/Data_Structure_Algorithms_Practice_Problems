# Output
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J

n = int(input("Enter the number of rows : "))
for i in range(n):
    for j in range(1, n+1):
        print(chr(64+j), end=' ')
    print()