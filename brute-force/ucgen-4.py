def ucgen4(x):
    for i in range(x):
        print(" " * (x-i-1) ,"*" * (i+1))

ucgen4(int(input()))