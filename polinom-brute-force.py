"""P = [1, -3, 2, 5]  # P(x) = x³ - 3x² + 2x + 5
x = 2 """

def polinom(P, x):
    result= 0
    for i in range(len(P)):
        result+= P[i] * x**(len(P)-i-1)
    return result

P = [1, -3, 2, 5] 
print(polinom(P,2))

