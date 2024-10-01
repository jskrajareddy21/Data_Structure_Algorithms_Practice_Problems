# Output
# J I H G F E D C B A
# J I H G F E D C B A
# J I H G F E D C B A
# J I H G F E D C B A
# J I H G F E D C B A
# J I H G F E D C B A
# J I H G F E D C B A
# J I H G F E D C B A
# J I H G F E D C B A
# J I H G F E D C B A

n = int(input("Enter the number of rows : "))
for i in range(n):
    for j in range(n,0,-1):
        print(chr(64+j), end=' ')
    print()