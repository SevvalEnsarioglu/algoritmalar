"""sıfır dısındaki rakamlardan olusan bir A dizisi veriliyor. bu dizinin 1 ile başlayan 9 ile biten ve ardışık terimlerden oluşan 
alt dizilerinin sayısını bulabilen algoritmalar tasarlayınız"""
#burada yapmamız gereken 1 lerin sa
def deneme1(A):
    count=0
    for i in range(len(A)):
        if(A[i]==1):
            for j in range(i+1, len(A)):
                if(A[j] == 9):
                    count+=1
    return count

"""bu kodu açıklayalım.a[i]=1 her bulduğumuz senaryoda ilerisinde kaç tane 9 olduğunu sayarız.bu doğrultuda count arttırırız."""

def deneme2(A):
    c=0
    c1=0
    for i in range(len(A)):
        if(A[i]==1):
            c1+=1
        if(A[i]==9):
            c+=c1 
    return c

#deneme2 deki amaç 1 lerin sayısını sayar, sonra 1 lerden sonra gördüğü her 9 da o 1 lerle oluşturduğu dizi için toplama yapar 
A= [2,3,1,1,5,7,9,1,8,9,6,1,9]
deneme2(A)
print(deneme2(A))


