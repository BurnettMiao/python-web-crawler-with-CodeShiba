import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.ptt.cc/bbs/NBA/index6502.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)

# print(response.text)

# if response.status_code == 200:
#   with open('output.html', 'w', encoding='utf-8') as f:
#     f.write(response.text)
#   print('寫入成功')
# else:
#   print('沒有抓到網頁')

soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('div', class_='r-ent')
data_list = []
# print(articles[0])
for a in articles:
  data = {}
  title = a.find('div', class_='title')
  if title and title.a:
    title = title.a.text
  else:
    title = '沒有標題'
  # print(title)
  data['標題'] = title

  popular = a.find('div', class_='nrec')
  if popular and popular.span:
    popular = popular.span.text
  else:
    popular = 'N/A'
  data['人氣'] = popular
  # print(f"標題:{title} 人氣:{popular}")

  date = a.find('div', class_='date')
  if date:
    date = date.text
  else:
    date = 'N/A'
  data['日期'] = date

  data_list.append(data)
  # print(f"標題: {title} 人氣:{popular} 日期:{date}")
# print(data_list)

df = pd.DataFrame(data_list)
df.to_excel('ptt_nba.xlsx', index=False, engine='openpyxl')