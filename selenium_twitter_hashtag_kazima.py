import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

kullanici_adi = input("Kullanıcı Adınız: ")
kullanici_sifresi = input("Şifreniz: ")
hedef = input("Hangi hashtag üzerinde işlem yapmak istiyorsanız başında # olmadan giriniz.Mesela btcusdt gibi: ")
if hedef[0] == "#":
    hedef = hedef[1:]

tweet_sayisi = int(input("En son atılan kaç tweeti görmek istiyorsunuz: "))
if (type(tweet_sayisi) != int) or (tweet_sayisi < 1):
    print("Tweet sayisi pozitif tam sayı olmak zorundadır")
    exit()

driver = webdriver.Chrome(".../chromedriver.exe")
url = "https://twitter.com/login"
driver.get(url)
time.sleep(3)

driver.maximize_window()
time.sleep(3)

giris = driver.find_element(By.XPATH,"//input[@autocomplete='username']")
giris.send_keys(kullanici_adi)
time.sleep(3)
giris.send_keys(Keys.ENTER)
time.sleep(3)

sifre = driver.find_element(By.XPATH,"//input[@autocomplete='current-password']")
sifre.send_keys(kullanici_sifresi)
time.sleep(3)
sifre.send_keys(Keys.ENTER)
time.sleep(3)

url2 = "https://twitter.com/search?q=%23{}&src=typed_query&f=live".format(hedef)
driver.get(url2)
time.sleep(3)

bilgi = []
profil = driver.find_elements(By.CSS_SELECTOR,".css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu")
for i in profil:
    bilgi.append(i.text)

while True:
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
    time.sleep(3)
    profil2 = driver.find_elements(By.CSS_SELECTOR, ".css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu")
    for i in profil2:
        x = i.text
        if x not in bilgi:
            bilgi.append(x)
    if len(bilgi) >= tweet_sayisi:
        break

j = 1
for i in range(0,tweet_sayisi):
    kisi_adi = (bilgi[i].split("\n")[1])
    kisi_tweeti = (bilgi[i].split("\n")[4])
    print(f"{j}-{kisi_adi}: {kisi_tweeti}")
    j += 1

input("Çıkmak için bir tuşa basınız")
driver.close()
exit()