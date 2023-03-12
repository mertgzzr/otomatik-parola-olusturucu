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
