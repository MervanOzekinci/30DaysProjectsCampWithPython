from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class weather:
    def __init__(self,city):
        self.url="https://www.mgm.gov.tr/?il="
        self.browser=webdriver.Chrome()
        self.city=city
    
    def cityWeaher(self):
        self.browser.get(self.url+self.city)
        time.sleep(2)
        celcius=self.browser.find_element_by_xpath("//*[@id='siteBody']/section[1]/div/div[2]/div[2]/div/h3/span[1]/ziko").text
        day=self.browser.find_element_by_xpath("//*[@id='siteBody']/section[1]/div/div[2]/div[2]/p").text
        info=self.browser.find_element_by_xpath("//*[@id='siteBody']/section[1]/div/div[2]/div[2]/div/p").text
        print(f"Gün: {day},sicaklik: {celcius},Hava Durumu: {info}")

        if info=="Sıcak":
            print("Allah yardimcin olsun. Serin bir yerde kal!")
            
        elif info=="Açık":
            print("Bugün hava güzel")
        elif info=="Parçalı Bulutlu":
            print("Bir semsiye yaninizda bulundurun her ihtimale karsi")
        elif info=="Mevzi Sağanak Yağışlı":
            print("Mutlaka bir semsiye bulundurun kendinizle")
       
        
veri=input("Hava Durumunu Ögrenmek Istediginiz Sehir Adi:")
sehir=weather(veri.capitalize())
sehir.cityWeaher()

sicaklik=sehir.cityWeaher()



    