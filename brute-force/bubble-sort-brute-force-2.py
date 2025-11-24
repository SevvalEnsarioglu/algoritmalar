def bubble2(A):
    for i in range(len(A)-1):
        print(f"i={i} döngüsündeyiz!")
        for j in range(len(A)-i-1):
            print(f"j={j} iken {A[j]} ve {A[j+1]} kiyaslanir")
            if (A[j] >A[j+1]):
                temp= A[j]
                A[j]= A[j+1]
                A[j+1] = temp
                print(f"A dizisi değişti: {A}")
            else:
                print("A dizisi degismedi...")
        print()
    return A


B = [3,9,7,6,5,1]
print(bubble2(B))

#içerideki döngüde range'in len(A)-i-1 olmasındaki i nin sebebi, her döngü itere edildiğinde sondaki en büyük değerin yerini bulmuş olması ve bir daha dokunmaya gerek duymayışımızdır
#her seferinde en büyük sayı doğru yere giderek sayılar yerleştirilir