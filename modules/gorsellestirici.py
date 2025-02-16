import pandas as pd
import matplotlib.pyplot as plt

def grafik_olustur(grafik_turu, veri_sozlugu):
    if not isinstance(veri_sozlugu, dict):
        raise ValueError("Veri sözlük formatında olmalıdır!")
    if grafik_turu == "sutun":
        df = pd.DataFrame(veri_sozlugu)
        if "isimler" in veri_sozlugu and "yaslar" in veri_sozlugu:
            df.plot(x="isimler", y="yaslar", kind='bar')
            plt.title("YiğitTools | Sütun Grafiği")
            plt.xlabel("İsimler")
            plt.ylabel("Yaşlar")
            plt.show()
            return "Grafik oluşturuldu"
    elif grafik_turu == "dagilim":
        df = pd.DataFrame(veri_sozlugu)
        if "x" in veri_sozlugu and "y" in veri_sozlugu:
            df.plot(x="x", y="y", kind='scatter')
            plt.title("YiğitTools | Dağılım Grafiği")
            plt.show()
            return "Grafik oluşturuldu"
    return "Desteklenmeyen grafik türü veya veri yapısı"