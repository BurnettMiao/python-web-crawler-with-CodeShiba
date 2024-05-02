import requests
from bs4 import BeautifulSoup
import pandas as pd

data_list = []

def fetch_data(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  movies = soup.find_all('section', class_='infoArea')
  for movie in movies:
    name = movie.find('a')
    name = name.text.strip() # 使用 .strip() 去除空格
    engName = movie.find('h3')
    engName = engName.text.strip()
    date = movie.find('time')
    date = date.text.strip()
    data_list.append([name, engName,date])
  print(data_list)

url = 'https://www.vscinemas.com.tw/vsweb/film/index.aspx'

fetch_data(url)

df = pd.DataFrame(data_list, columns=['中文電影名稱', '英文電影名稱', '上映日期'])
df.to_excel('現正熱映.xlsx', index=False, engine='openpyxl')