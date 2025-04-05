import colorama
from typing import Dict, Any
from concurrent.futures import ThreadPoolExecutor
from modules.rastgele import rastgele_sayi, rastgele_metin
from modules.gorsellestirici import grafik_olustur
import time
import sys
import platform
import os
import modules.tarayici as tarayici
import modules.web_istekleri as web_istekleri
import modules.seri_iletisim
import sys
import argparse

parser = argparse.ArgumentParser(description="YiğitTools - Python ile yazılmış bir otomasyon aracı")
parser.add_argument("--yapi", help="Yeni bir proje yapısı oluşturur", action="store_true")
argumanlar = parser.parse_args()

colorama.init(autoreset=True)

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
            'grafik': grafik_olustur,
            'tarayici_ac': tarayici.siteye_gir,
            'tarayici_kapat': tarayici.siteyi_kapat,
            'tikla': tarayici.siteyi_tikla,
            'yaz': tarayici.siteye_yaz,
            'oku': tarayici.siteyi_oku,
            'bekle': tarayici.siteyi_beklet,
            'fare_tasi': tarayici.siteyi_tasi,
            'kaydir': tarayici.siteyi_kaydir,
            'geri': tarayici.siteyi_geri_al,
            'ileri': tarayici.siteyi_ileri_al,
            'yenile': tarayici.siteyi_yenile,
            'ekran_buyut': tarayici.siteyi_ekrana_al,
            'ekran_kucult': tarayici.siteyi_kucult,
            'tam_ekran': tarayici.siteyi_tam_ekran_yap,
            'ekran_kaydet': tarayici.siteyi_ekrani_kaydet,
            'ekran_goster': tarayici.siteyi_ekrani_goster,
            'html_al': web_istekleri.html_cek,
            'baslik_al': web_istekleri.baslik_cek,
            'link_al': web_istekleri.link_cek,
            'resim_al': web_istekleri.resim_cek,
            'metin_al': web_istekleri.metin_cek,
            'baslik_ara': web_istekleri.baslik_ara,
            'metin_ara': web_istekleri.metin_ara,
            'etiket_ara': web_istekleri.etiket_ara,
            'etiket_ara_ozellik': web_istekleri.etiket_ara_ozellik,
            'etiket_ara_ozellik_deger': web_istekleri.etiket_ara_ozellik_deger,
            'seri_baslat': modules.seri_iletisim.seri_iletisim,
            'seri_porta_yaz': modules.seri_iletisim.seri_yaz,
            'seri_porttan_oku': modules.seri_iletisim.seri_oku,
            'seri_kapat': modules.seri_iletisim.seri_kapat
        }

    def sozluk_ayristir(self, metin: str) -> dict:
        try:
            tek_satir = metin.replace('\n', '').strip()
            izin_verilen = set('{}[]:," 0123456789abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ')
            if not all(c in izin_verilen for c in tek_satir):
                raise ValueError("Geçersiz karakterler")
            return eval(tek_satir, {"__builtins__": {}}, {})
        except Exception as e:
            raise ValueError(f"Sözlük ayrıştırma hatası: {str(e)}")

    def satir_isle(self, satir: str):
        if not satir.strip() or satir.startswith('!'):
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
                if (param.startswith('"') and param.endswith('"')) or (param.startswith("'") and param.endswith("'")):
                    param = param[1:-1]
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
    print(colorama.Fore.GREEN + colorama.Style.BRIGHT + """
__   _____ ____ ___ _____   _____ ___   ___  _     ____  
\ \ / /_ _/ ___|_ _|_   _| |_   _/ _ \ / _ \| |   / ___| 
 \ V / | | |  _ | |  | |     | || | | | | | | |   \___ \ 
  | |  | | |_| || |  | |     | || |_| | |_| | |___ ___) |
  |_| |___\____|___| |_|     |_| \___/ \___/|_____|____/ 
          
YigitRobotics Tarafından Oluşturuldu. \n
""")
    dosya_yolu = input("Dosya yolu: ")
    if not dosya_yolu.endswith('.ygtools'):
        print(colorama.Fore.RED + "Hata: Sadece .ygtools uzantılı dosyalar desteklenir!" + colorama.Style.RESET_ALL)
        return
    girdi_al(dosya_yolu)

def platform_belirle():
    if platform.system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def hazirla():
    platform_belirle()
    for _ in range(4):
        print("YiğitTools yükleniyor.")
        time.sleep(0.4)
        platform_belirle()
        print("YiğitTools yükleniyor..")
        time.sleep(0.4)
        platform_belirle()
        print("YiğitTools yükleniyor...")
        time.sleep(0.4)
        platform_belirle()
    platform_belirle()
    print("YiğitTools başlatılıyor...")
    time.sleep(1)
    platform_belirle()
    print("YiğitTools hazır!")
    time.sleep(1)
    platform_belirle()
    ana_program()

def platform_belirle2():
    if platform.system == "Windows":
        return "COM3"
    else:
        return "/dev/ttyUSB0"

if argumanlar.yapi:
    seri_port = platform_belirle2()
    print(colorama.Fore.GREEN + "Basit bir yapı oluşturuluyor..." + colorama.Fore.RESET)
    time.sleep(3)
    platform_belirle()
    os.makedirs("YGtools", exist_ok=False)
    os.makedirs("YGtools/modules", exist_ok=False)

    with open("ygtools/main.ygtools", "w", encoding="utf-8") as dosya:
        dosya.write('''! Bu dosya YiğitTools için örnek bir dosyadır.
yazdir::"Merhaba, dünya!"
        ''')
    with open("ygtools/modules/seri_port_islemleri.ygtools", "w", encoding="utf-8") as dosya2:
        dosya2.write(f'''! Bu dosya YiğitTools için örnek bir modül dosyasıdır.
seri_baslat::"{seri_port}" $ 9600
        ''')

if __name__ == "__main__":
    hazirla()
else:
    print("Bu dosya modül olarak kullanılamaz!", file=sys.stderr)
    sys.exit(1)