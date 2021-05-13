import requests
from bs4 import BeautifulSoup
import os
import pyautogui as p
from time import sleep

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'}
clear = "clear"

while True:

    curs1 = 'https://www.google.com/search?client=firefox-b-d&biw=1841&bih=945&sxsrf=ALeKk00S9BhtHUrBZUHmc68MR8BA97lQRQ%3A1610445524653&ei=1HL9X6CfJ_6MwPAPza-O6AM&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0+%D0%BD%D0%B0+%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F+%D0%B2+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0%D1%85&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0+%D0%BD%D0%B0+%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F+&gs_lcp=CgZwc3ktYWIQAxgAMgIIADICCAAyAggAMgIIADICCAAyBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BAgAEEdQrSVYrSVg-jZoAHACeACAAZ4DiAGeA5IBAzQtMZgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab'
    curs = 'https://ru.investing.com/crypto/bitcoin/btc-usd'
    
    page1 = requests.get(curs1, headers=headers)
    soup1 = BeautifulSoup(page1.content, 'html.parser')
    convert1 = soup1.find("span", {'class':'DFlfde', 'class':'SwHCTb', 'data-precision':'2'})


    page = requests.get(curs, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    convert = soup.find("span", {'class':'arial_20', 'class':'pid-945629-pc'})
    convert2 = soup.find("span", {'class':'arial_20', 'class':'pid-945629-pcp', 'class':'parentheses'})



    os.system(clear)
    print("Курс Биткоина на сегодня составляет " + convert1.text + "$" + "\n" + "Статистика: " + convert.text + " (" + convert2.text + ")")
