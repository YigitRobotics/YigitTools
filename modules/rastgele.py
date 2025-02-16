import random
import string

def rastgele_sayi(alt_sinir, ust_sinir):
    return random.randint(alt_sinir, ust_sinir)

def rastgele_metin(uzunluk, karakterler=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(karakterler) for _ in range(uzunluk))