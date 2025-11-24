def matris_carpimi(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])

    C = [[0 for i in range(p)] for i in range(m)] #p tane 0 lı sütün oluşturma ve bunlardan m tane satır olması

    for i in range(m):  #a nın her satırı için döngü açtık   
        for j in range(p): #b nin her sütunu için döngü açtık
            C[i][j] = 0 # mxp lik c matrisini başta bu konumda sıfırlıyoruz
            for k in range(n): # a nın sütunu ve b nin satırı (aynı uzunluktalar) her biri için aynı index e tekabul edenleri çarpıyoruz ve C matrisinin i ve j bakımından denk gelen noktasına toplama olarak bu çarpımları ekleyerek C matrisini inşa ediyoruz
                C[i][j] += A[i][k] * B[k][j]
    return C

E = [[1, 2],
     [3, 4]]

F = [[5, 6],
     [7, 8]]

print(matris_carpimi(E, F))
