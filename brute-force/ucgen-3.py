def ucgen3(x):
    for i in range(x):
        print(" " * (x-i-1), "*"*(i+1))

ucgen3(int(input()))