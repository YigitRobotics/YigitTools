import requests
import colorama
from bs4 import BeautifulSoup

def html_cek(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return colorama.Fore.BLUE + soup.prettify()
def baslik_cek(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.title.string
def link_cek(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links
def resim_cek(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    images = []
    for img in soup.find_all('img'):
        images.append(img.get('src'))
    return images
def metin_cek(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.get_text()
def baslik_ara(url, baslik):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.find_all('title', string=baslik)
def metin_ara(url, metin):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.find_all(string=metin)
def etiket_ara(url, etiket):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.find_all(etiket)
def etiket_ara_ozellik(url, etiket, ozellik):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.find_all(etiket, class_=ozellik)
def etiket_ara_ozellik_deger(url, etiket, ozellik, deger):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.find_all(etiket, {ozellik: deger})