"""ana fikir dizinin en küçük elemanını bulup ilk elemanla yer değiştirmektir. sonra aynı işlemleri 
dizinin 2,3,4,5... n-1 elemanından başlayarak uygulamaktır """

def selection_sort(P): 
    for i in range(len(P)): 
        min=i
        for j in range(len(P)-i):
            if(P[j+i]<P[min]):
                min = j+i
        temp = P[i]
        P[i] = P[min]
        P[min] = temp
    return P

"""bu algoritmayı açıklayalım: P dizisi uzunluğunda bir döngü açıyoruz. i değerini min seçiyoruz. 2 bir döngü ile i nin bulunduğu 
konumun ilerisi kadarki yeri kontrol ediyoruz. i nin bulunduğu noktanın ilerisinden sonuna kadar kontrol edip min değerini buluyoruz
her seferinde min ile i nin olduğu yeri değiştirerek küçük sayıları sola kaydırıyoruz adım adım. bu şekilde sıralama yapıyoruz."""

""" def selection_sort(P):
    for i in range(len(P)):
        min = i
        for j in range(i+1, len(P)):  # ← BURASI FARKLI
            if(P[j] <= P[min]):
                min = j
        temp = P[i]
        P[i] = P[min]
        P[min] = temp
        print(P)
    return P"""

F = [9,6,5,7,8]

print(selection_sort(F))