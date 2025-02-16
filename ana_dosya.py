import string
import random
import colorama
import os
import matplotlib.pyplot as plt
import pandas as pd
from typing import Dict, Any
import requests # sonra kullanacam
import socket # sonra kullanacam
from concurrent.futures import ThreadPoolExecutor # sonra kullanacam
import selenium.webdriver # sonra kullanacam

def rastgele_sayi(alt_sinir, ust_sinir):
    return random.randint(alt_sinir, ust_sinir)

def rastgele_metin(uzunluk, karakterler=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(karakterler) for _ in range(uzunluk))

class YGToolsYorumlayici:
    def __init__(self):
        self.degiskenler: Dict[str, Any] = {}
        self.komutlar = {
            'rastgele_sayi': rastgele_sayi,
            'rastgele_metin': rastgele_metin,
            'yazdir': print,
            'topla': lambda x, y: x + y,
            'cikar': lambda x, y: x - y,
            'carp': lambda x, y: x * y,
            'bol': lambda x, y: x / y,
            'grafik': self.grafik_olustur
        }

    def sozluk_ayristir(self, metin: str) -> dict:
        """Çok satırlı sözlük tanımlamalarını işler"""
        try:
            tek_satir = metin.replace('\n', '').strip()
            izin_verilen = set('{}[]:," 0123456789abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ')
            if not all(c in izin_verilen for c in tek_satir):
                raise ValueError("Geçersiz karakterler")
            return eval(tek_satir, {"__builtins__": {}}, {})
        except Exception as e:
            raise ValueError(f"Sözlük ayrıştırma hatası: {str(e)}")

    def grafik_olustur(self, grafik_turu, veri_sozlugu):
        if not isinstance(veri_sozlugu, dict):
            raise ValueError("Veri sözlük formatında olmalıdır!")
            
        if grafik_turu == "sutun":
            veri_cercevesi = pd.DataFrame(veri_sozlugu)
            if "isimler" in veri_sozlugu and "yaslar" in veri_sozlugu:
                veri_cercevesi.plot(x="isimler", y="yaslar", kind='bar')
                plt.title("YiğitTools | Sütun Grafiği")
                plt.xlabel("İsimler")
                plt.ylabel("Yaşlar")
                plt.show()
                return "Grafik oluşturuldu"
        elif grafik_turu == "dagilim":
            veri_cercevesi = pd.DataFrame(veri_sozlugu)
            if "x" in veri_sozlugu and "y" in veri_sozlugu:
                veri_cercevesi.plot(x="x", y="y", kind='scatter')
                plt.title("YiğitTools | Dağılım Grafiği")
                plt.show()
                return "Grafik oluşturuldu"
        return "Desteklenmeyen grafik türü veya veri yapısı"

    def satir_isle(self, satir: str):
        if not satir.strip() or satir.startswith('#'):
            return None
        
        try:
            if '=' in satir:
                degisken_adi, ifade = satir.split('=', 1)
                degisken_adi = degisken_adi.strip()
                ifade = ifade.strip()

                if ifade.startswith('{'):
                    sozluk_tamam = False
                    tam_sozluk = ifade
                    kapanan_suzluk_sayisi = ifade.count('}')
                    acilan_suzluk_sayisi = ifade.count('{')
                    
                    if kapanan_suzluk_sayisi == acilan_suzluk_sayisi:
                        sozluk_tamam = True
                    
                    if sozluk_tamam:
                        sonuc = self.sozluk_ayristir(tam_sozluk)
                    else:
                        return None
                else:
                    sonuc = self.ifade_degerlendir(ifade)
                
                self.degiskenler[degisken_adi] = sonuc
                return f"{degisken_adi} = {sonuc}"
            else:
                return self.ifade_degerlendir(satir)
        except Exception as hata:
            return f"Hata: {str(hata)}"

    def ifade_degerlendir(self, ifade: str):
        if "::" not in ifade:
            return self.degiskenler.get(ifade.strip(), f"Değişken bulunamadı: {ifade}")
        
        komut, parametreler = ifade.split("::", 1)
        komut = komut.strip()
        parametreler = parametreler.strip()

        if komut not in self.komutlar:
            raise ValueError(f"Bilinmeyen komut: {komut}")
        
        islenmis_parametreler = []
        if parametreler:
            for param in parametreler.split("$"):
                param = param.strip()
                if param in self.degiskenler:
                    islenmis_parametreler.append(self.degiskenler[param])
                else:
                    try:
                        islenmis_parametreler.append(float(param) if '.' in param else int(param))
                    except ValueError:
                        islenmis_parametreler.append(param)

        return self.komutlar[komut](*islenmis_parametreler)

def girdi_al(dosya_yolu):
    yorumlayici = YGToolsYorumlayici()
    
    with open(dosya_yolu, "r", encoding="utf-8") as girdi_dosyasi:
        print(colorama.Fore.CYAN + "\nProgram çıktısı:" + colorama.Style.RESET_ALL)
        for satir_numarasi, satir in enumerate(girdi_dosyasi, 1):
            satir = satir.strip()
            if satir:
                sonuc = yorumlayici.satir_isle(satir)
                if sonuc is not None:
                    print(f"{colorama.Fore.YELLOW}Satır {satir_numarasi}:{colorama.Style.RESET_ALL} {sonuc}")

def ana_program():
    print(colorama.Fore.GREEN, colorama.Style.BRIGHT + """
__   _____ ____ ___ _____   _____ ___   ___  _     ____  
\ \ / /_ _/ ___|_ _|_   _| |_   _/ _ \ / _ \| |   / ___| 
 \ V / | | |  _ | |  | |     | || | | | | | | |   \___ \ 
  | |  | | |_| || |  | |     | || |_| | |_| | |___ ___) |
  |_| |___\____|___| |_|     |_| \___/ \___/|_____|____/ 
          

Oxcanga Tarafından Oluşturuldu. \n
""")
    dosya_yolu = input("Dosya yolu: ")
    if not dosya_yolu.endswith('.ygtools'):
        print(colorama.Fore.RED + "Hata: Sadece .ygtools uzantılı dosyalar desteklenir!" + colorama.Style.RESET_ALL)
        return
    girdi_al(dosya_yolu)
    
ana_program()