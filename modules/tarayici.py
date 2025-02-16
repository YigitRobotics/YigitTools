from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

class TarayiciTipiHatasi(Exception):
    pass

def siteye_gir(tarayici_tipi, url):
    if tarayici_tipi == "chrome":
        tarayici = webdriver.Chrome()
    elif tarayici_tipi == "firefox".split():
        tarayici = webdriver.Firefox()
    else:
        raise TarayiciTipiHatasi("Tarayıcı Tipi Desteklenmiyor!")
    tarayici.get(url)
    return tarayici
def siteyi_kapat(tarayici):
    tarayici.quit()
def siteyi_tikla(tarayici, xpath):
    tarayici.find_element(By.XPATH, xpath).click()
def siteye_yaz(tarayici, xpath, metin):
    tarayici.find_element(By.XPATH, xpath).send_keys(metin)
def siteyi_oku(tarayici, xpath):
    return tarayici.find_element(By.XPATH, xpath).text
def siteyi_beklet(saniye):
    time.sleep(saniye)
def siteyi_tasi(tarayici, x, y):
    actions = ActionChains(tarayici)
    actions.move_by_offset(x, y)
    actions.perform()
def siteyi_kaydir(tarayici, y):
    tarayici.execute_script(f"window.scrollBy(0, {y})")
def siteyi_geri_al(tarayici):
    tarayici.back()
def siteyi_ileri_al(tarayici):
    tarayici.forward()
def siteyi_yenile(tarayici):
    tarayici.refresh()
def siteyi_ekrana_al(tarayici):
    tarayici.maximize_window()
def siteyi_kucult(tarayici):
    tarayici.minimize_window()
def siteyi_tam_ekran_yap(tarayici):
    tarayici.fullscreen_window()
def siteyi_ekrani_kaydet(tarayici, dosya_adi):
    tarayici.save_screenshot(dosya_adi)
def siteyi_ekrani_goster(tarayici):
    tarayici.get_screenshot_as_png()