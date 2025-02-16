# YGTools Programlama Dili

YGTools, temel matematiksel işlemler, rastgele değer üretimi ve grafik oluşturma gibi işlemleri basit bir sözdizimi ile yapmanıza olanak sağlayan bir programlama dilidir.

## Özellikler

- Basit ve anlaşılır sözdizimi
- Temel matematiksel işlemler (toplama, çıkarma, çarpma, bölme)
- Rastgele sayı ve metin üretimi
- Grafik oluşturma desteği (sütun ve dağılım grafikleri)
- Değişken tanımlama ve kullanma
- Sözlük veri yapısı desteği

## Komutlar

### Temel Komutlar
- `rastgele_sayi:: alt_sinir $ ust_sinir` - Belirtilen aralıkta rastgele sayı üretir
- `rastgele_metin:: uzunluk` - Belirtilen uzunlukta rastgele metin üretir
- `yazdir:: mesaj` - Ekrana mesaj yazdırır
- `topla:: sayi1 $ sayi2` - İki sayıyı toplar
- `cikar:: sayi1 $ sayi2` - İki sayının farkını alır
- `carp:: sayi1 $ sayi2` - İki sayıyı çarpar
- `bol:: sayi1 $ sayi2` - İki sayının bölümünü alır

### Grafik Komutları
- `grafik:: "sutun" $ veri_sozlugu` - Sütun grafiği oluşturur
- `grafik:: "dagilim" $ veri_sozlugu` - Dağılım grafiği oluşturur

## Kullanım Örneği

```
# Temel işlemler
sayi1 = rastgele_sayi:: 1 $ 100
sayi2 = rastgele_sayi:: 1 $ 100
toplam = topla:: sayi1 $ sayi2
yazdir:: toplam

# Grafik oluşturma
veriler = {"isimler": ["Ali", "Veli", "Ayşe"], "yaslar": [25, 30, 28]}
grafik:: "sutun" $ veriler
```

## Dosya Uzantısı

YGTools programları `.ygtools` uzantılı dosyalarda yazılır.

## Gereksinimler

- Python 3.x
- colorama
- matplotlib
- pandas
- typing

## Kurulum

1. Gerekli Python paketlerini yükleyin:
```bash
pip install colorama matplotlib pandas
```

2. YGTools dosyasını indirin ve çalıştırın:
```bash
python ana_dosya.py
```

3. Program çalıştığında `.ygtools` uzantılı dosyanızın yolunu girin.

## Dikkat Edilmesi Gerekenler

- Sadece `.ygtools` uzantılı dosyalar çalıştırılabilir
- Sözlük tanımlamaları geçerli Python sözlük formatında olmalıdır
- Grafik oluşturmak için veriler uygun formatta sözlük olarak tanımlanmalıdır
