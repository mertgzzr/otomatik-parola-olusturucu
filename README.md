# otomatik-parola-olusturucu
İşte Python'da rasgele sayı üretmek için birkaç farklı yöntem:
# 1.'random' modülü kullana;
 
 import random

 0 ile 100 arasında bir tam sayı üret
number = random.randint(0, 100)
print(number)

0.0 ile 1.0 arasında bir ondalıklı sayı üret
number = random.random()
print(number)

 Belirtilen bir aralıkta bir ondalıklı sayı üret
number = random.uniform(0, 10)
print(number)


# 1.'Numpy' mödülü kullanrak;
 
 import numpy as np

 0 ile 100 arasında bir tam sayı üret
number = np.random.randint(0, 100)
print(number)

 0.0 ile 1.0 arasında bir ondalıklı sayı üret
number = np.random.random()
print(number)

 Belirtilen bir aralıkta bir ondalıklı sayı üret
number = np.random.uniform(0, 10)
print(number)


Bu kodlar, random ve numpy modüllerini kullanarak rasgele sayılar üretir. random.randint(a, b) fonksiyonu, a ve b arasında bir tam sayı üretirken, random.random() fonksiyonu 0.0 ile 1.0 arasında bir ondalıklı sayı üretir. random.uniform(a, b) fonksiyonu ise, a ve b arasında bir ondalıklı sayı üretir.

numpy modülü, bilimsel hesaplama ve sayısal işlemler için kullanışlı bir kütüphanedir ve rasgele sayılar üretmek için de kullanılabilir. numpy.random modülü, random modülündeki fonksiyonlara benzer fonksiyonlara sahiptir.
