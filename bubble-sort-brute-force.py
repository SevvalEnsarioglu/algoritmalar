"""bubble sort: diziyi baştan sona tarayalım, ardışık ikilileri karşılaştıralım,
eğer sağdaki daha büyükse yerlerini değiştirelim. 
bu işlem sonucunda küçük sayı dizinin sağında olacak. """

def bubble_sort(A): 
    for i in range(len(A)-1): # listenin uzunluğunun 1 eksiğince bir döngü açıyoruz. 
        for j in range(len(A)-i-1): # yukarıdaki döngü her döndüğünde bu döngü, yukarıdakinin değerinin 1 eksiğinin yukarıdaki değer kadar eksiği kez dönecek
            temp=0
            if(A[j]> A[j+1]):
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    return A

B = [3,9,7,6,5,1]
print(bubble_sort(B))

#içerideki döngü yan yana ikilileri adım adım karşılaştıracak. eğer sağdaki daha büyükse ileri taşıyacak. 

"""B örneği üzerinden durumu analiz edelim.
i=0 iken j döngüsü 5 kere dönecek. j döngüsünün 5 kere dönüşünde olacaklar:
başlangıç: [3,9,7,6,5,1]
j=1 1. dönüş: [3,9,7,6,5,1] 3 ve 9 karşılaştırıldı, değişmedi
j=2 2. dönüş: [3,7,9,6,5,1] 9 ve 7 karşılaştırıldı, değişti
j=3 3. dönüş: [3,7,6,9,5,1] 9 ve 6 karşılaştırıldı, değişti
j=4 4. dönüş: [3,7,6,5,9,1] 5 ve 9 karşılaştırıldı, değişti
j=5 5. dönüş: [3,7,6,5,1,9] 9 ve 1 karşılaştırıldı, değişti
bu döngüde 9 en büyük sayı olarak en sağa kaydı. buradan anladığımız, içerideki döngüde range'in len(A)-i-1 olmasındaki i nin sebebi, her döngü itere edildiğinde sondaki en büyük değerin yerini bulmuş olması ve bir daha dokunmaya gerek duymayışımızdır

i=1 iken j döngüsü 4 kere dönecek. j döngüsünün 4 kere dönüşünde olacaklar:
başlangıç: [3,7,6,5,1,9]
j=0: [3,7,6,5,1,9] 3 ve 7 karşılaştırıldı, değişmedi
j=1: [3,6,7,5,1,9] 7 ve 6 karşılaştırıldı, değişti
j=2: [3,6,5,7,1,9] 


"""
