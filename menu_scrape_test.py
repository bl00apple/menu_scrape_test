import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np
from html.parser import HTMLParser
from openpyxl import Workbook
import xlsxwriter

wb = Workbook()
ws = wb.active
ws['A1'] = "image_url"

url = urlopen('http://www.oksfood.com/name/jp_name_a.html')
soup = BeautifulSoup(url.read(), 'html.parser')
table = soup.find_all('table', {"border":"1"})
for i in table:
    get_td = i.find_all('td', {"rowspan":"4"})
    for j in get_td:
        image_url = j.find('a')['href']
        image_url = image_url.replace("../", "") 
        image_url = "http://www.oksfood.com/"+image_url
        #print(image_url)
        ws.append([image_url])

wb.save("image_url_test_final.xlsx")





             


