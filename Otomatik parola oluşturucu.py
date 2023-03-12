import random
import string

def generate_password(length):
    """Belirtilen uzunlukta rasgele bir şifre oluşturur."""
    # Kullanılacak karakterlerin listesi
    chars = string.ascii_letters + string.digits + string.punctuation
    # Şifre oluşturma
    password = ''.join(random.choice(chars) for i in range(length))
    return password

# 10 karakter uzunluğunda bir şifre oluştur
password = generate_password(10)
print(password)
print(mertgzzr)
