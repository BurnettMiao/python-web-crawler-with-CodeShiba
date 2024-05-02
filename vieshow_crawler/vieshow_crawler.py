import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

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

  allPageList = soup.find('section', class_='pagebar')
  allPageList = allPageList.find_all('a')
  maxNum = len(allPageList) - 1
  minNum = len(allPageList) - (len(allPageList) - 1)
  for index in range(minNum, maxNum):
    print(index)
    newUrl = f'{url}?p=index'
    time.sleep(5)
    if index < maxNum:
      fetch_data(newUrl)

  # time.sleep(2)
  # print(minIndex, maxIndex)
  
url = 'https://www.vscinemas.com.tw/vsweb/film/index.aspx'

fetch_data(url)

# df = pd.DataFrame(data_list, columns=['中文電影名稱', '英文電影名稱', '上映日期'])
# df.to_excel('現正熱映.xlsx', index=False, engine='openpyxl')