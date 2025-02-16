# YGTools Programlama Dili

YGTools, temel matematiksel işlemler, rastgele değer üretimi, grafik oluşturma, seri porta yazı yazma ve web sitesinden veri çekme gibi işlemleri basit bir sözdizimi ile yapmanıza olanak sağlayan bir programlama dilidir.

## Özellikler

- Basit ve anlaşılır sözdizimi
- Temel matematiksel işlemler (toplama, çıkarma, çarpma, bölme)
- Rastgele sayı ve metin üretimi
- Grafik oluşturma desteği (sütun ve dağılım grafikleri)
- Değişken tanımlama ve kullanma
- Sözlük veri yapısı desteği
- Seri porta yazı yazma (pyserial)
- Web sitesinden veri çekme ve HTTP isteği gönderme (bs4 ve requests)
- Tarayıcı otomasyonu ve özellikleri (selenium)

## Kullanım Örneği

```python
! Temel işlemler
sayi1 = rastgele_sayi:: 1 $ 100
sayi2 = rastgele_sayi:: 1 $ 100
toplam = topla:: sayi1 $ sayi2
yazdir:: toplam

! Grafik oluşturma
veriler = {"isimler": ["Ali", "Veli", "Ayşe"], "yaslar": [25, 30, 28]}
grafik:: "sutun" $ veriler

! tarayıcı işlemleri
tarayicim = tarayici_ac::chrome$"https://www.example.com"
yazdir::"Html çekiliyor \n"
html_al::"https://www.example.com"
yazdir::"Html alındı \n"

! seri port işlemleri
ser_conn=seri_baslat::"COM3"$9600 ! COM3 portunu değiştirebilirsiniz.
seri_porta_yaz::ser_conn$"Merhaba, seri bağlantı aktif!"
gelen=seri_porttan_oku::ser_conn
yazdir::gelen
seri_kapat::ser_conn
```

## Dosya Uzantısı

YGTools programları `.ygtools` uzantılı dosyalarda yazılır.

## Gereksinimler

- Python 3.x
- colorama
- matplotlib
- pandas
- typing
- selenium
- requests
- bs4 (BeautifulSoup)
- pyserial

## Kurulum

1. Gerekli Python paketlerini yükleyin:
```bash
pip install -r requirements.txt
```

2. YGTools dosyasını indirin ve çalıştırın:
```bash
python ana_dosya.py
```

3. Program çalıştığında `.ygtools` uzantılı dosyanızın yolunu girin.

## Dikkat Edilmesi Gerekenler

- Sadece `.ygtools` uzantılı dosyalar çalıştırılabilir.
- Sözlük tanımlamaları geçerli Python sözlük formatında olmalıdır.
- Grafik oluşturmak için veriler uygun formatta sözlük olarak tanımlanmalıdır.