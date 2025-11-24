# Algoritmalar

Bilgisayar algoritması, bir problemin **bilgisayar yardımıyla sonlu zamanda** çözülebilmesini sağlayan, **adım adım tanımlanmış talimatlar dizisidir**. Algoritma, girdileri (input) alıp istenen çıktılara (output) dönüştürür.

---

## Problem Çözme Aşamaları

1. **Problemi anlama**
2. **Çözüm stratejisi belirleme**
3. **Algoritma tasarımı**

   * a. Adım adım anlatım
   * b. Sözde kod (pseudocode)
4. **Algoritma analizi**

   * a. Algoritmanın doğruluğunun ispatı
   * b. Algoritma analizi (zaman ve bellek karmaşıklığı)
5. **Bilgisayar kodunu yazma**

---

## Algoritma Tasarlama Yöntemleri

### 1. **Kaba Kuvvet (Brute Force)**

Tüm olası çözümleri tek tek deneyerek doğru sonuca ulaşmayı amaçlar.

### 2. **Böl ve Yönet (Divide and Conquer)**

Problemi daha küçük alt problemlere ayırır, çözer ve birleştirir.

### 3. **Azalt ve Yönet (Decrease and Conquer)**

Problemi her adımda bir miktar küçülterek çözer (örneğin n → n-1).

### 4. **Dönüştür ve Yönet (Transform and Conquer)**

Problemi daha kolay çözülebilecek başka bir forma dönüştürür.

### 5. **Hafıza – Zaman Takası**

Daha hızlı çözmek için daha fazla bellek kullanma (veya tam tersi).

### 6. **Dinamik Programlama**

Alt problemlerin sonuçlarını saklayarak tekrar hesaplamanın önüne geçer.

### 7. **Açgözlü Yaklaşım (Greedy Approach)**

Her adımda yerel olarak en iyi görünen seçimi yaparak çözümü üretmeye çalışır.

---

> **Not:** Birden fazla yöntem olmasının sebebi, her problemin yapısının farklı olması ve her yöntemle aynı verimlilikte çözülememesidir.

---

## Asimptotik Analiz - O, Θ, Ω Gösterimleri

Algoritmanın performansını değerlendirmek için kullanılan asimptotik gösterimler şunlardır:

### **f(n) = O(g(n))** — Üst Sınır (Big O)
f(n)'in büyük n değerleri için g(n) ile sınırlı olduğu anlamına gelir. Algoritmanın **en kötü durumda** ne kadar zaman aldığını gösterir. c > 0 ve n₀ > 0 için: **0 ≤ f(n) ≤ c·g(n)** (n ≥ n₀ için)

### **f(n) = Θ(g(n))** — Sıkı Sınır (Theta)
f(n) ve g(n)'in **aynı büyüme oranında** olduğu anlamına gelir. Algoritmanın davranışını en kesin şekilde tanımlar. c₁ > 0 ve c₂ > 0 için: **c₁·g(n) ≤ f(n) ≤ c₂·g(n)**

### **f(n) = Ω(g(n))** — Alt Sınır (Omega)
f(n)'in g(n) kadar hızlı büyüdüğü anlamına gelir. Algoritmanın **en iyi durumda** ne kadar zaman aldığını gösterir. c > 0 için: **f(n) ≥ c·g(n)**

### **f(n) = o(g(n))** — Katı Üst Sınır (Little o)
f(n)'in g(n)'den **kesinlikle daha yavaş** büyüdüğü anlamına gelir. **ω > 0**

### **f(n) = ω(g(n))** — Katı Alt Sınır (Little omega)
f(n)'in g(n)'den **kesinlikle daha hızlı** büyüdüğü anlamına gelir. **ω > 1**

---

## Karmaşıklık Sınıfları (En Aza Göre)

1. **O(1)** — Sabit zaman (Constant)
2. **O(log n)** — Logaritmik
3. **O(n)** — Doğrusal
4. **O(n log n)** — Linearitmik
5. **O(n²)** — Karesel
6. **O(n³)** — Kübik
7. **O(2ⁿ)** — Üstel
8. **O(n!)** — Faktöriyel

---

## Asimptotik Karşılaştırmanın Özellikleri

### 1. **Geçişkenlik (Transitivity)**

Tüm karşılaştırmalarda geçişkenlik var:

- Eğer f(n) = O(g(n)) ve g(n) = O(h(n)) ise → **f(n) = O(h(n))**
- Eğer g(n) = O(h(n)) ise → **f(n) = O(h(n))**

### 2. **Yansıma Özelliği (Reflexivity - Kendisini Gömme)**

f(n) = O(f(n))

f(n) = Θ(f(n))

f(n) = Ω(f(n))

### 3. **Simetri Özelliği (Symmetry - Order Θ)**

f(n) = Θ(g(n)) ise → **g(n) = Θ(f(n))**

### 4. **Ters Simetri (Transpose Symmetry)**

f(n) = O(g(n)) ise → **g(n) = Ω(f(n)) dir**

f(n) = o(g(n)) ise → **g(n) = ω(f(n)) dir**

---

**Not:** α₀ ve W parametreleri için:
- α₀ ve Ω seçiminde geçerli sabitleri bulunmalıdır
- f(n) = O(g(n)) ise g(n) = Ω(f(n)) dir
- f(n) = o(g(n)) ise g(n) = ω(f(n)) dir

---

**Her algoritmayı tasarlarken amacımız verilen problemin kısıtları altında en düşük karmaşıklıkla çözümü elde etmektir.**

