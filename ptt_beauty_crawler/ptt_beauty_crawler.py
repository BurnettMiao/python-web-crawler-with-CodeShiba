import requests
from bs4 import BeautifulSoup
import os # 建立資料夾套件

def download_img(url, save_path):
  print(f"正在下載圖片: {url}")
  response = requests.get(url)
  with open(save_path, 'wb') as file:
    file.write(response.content)
  print('-' * 30)

def main():
  url = 'https://www.ptt.cc/bbs/Beauty/M.1686997472.A.FDA.html'
  headers = {'Cookie': '_gid=GA1.2.186421156.1714373057; _gat=1; over18=1; _ga_DZ6Y3BY9GW=GS1.1.1714439650.10.1.1714439651.0.0.0; _ga=GA1.1.167492845.1711588536', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.text, 'html.parser')
  # print(soup.prettify())
  spans = soup.find_all('span', class_='article-meta-value')
  # print(spans[2].text)
  title = spans[2].text

  # 1. 建立一個圖片資料夾
  dir_name = f"ptt_beauty_crawler/images/{title}"
  if not os.path.exists(dir_name):
    os.makedirs(dir_name)

  # 2. 找到網頁中的所有連結
  links = soup.find_all('a')
  allow_file_name = ['jpg', 'png', 'jpeg', 'gif']
  for link in links:
    href = link.get('href')
    if not href:
      continue
    file_name = href.split('/')[-1]
    extension = href.split('.')[-1].lower()
    # print(extension)
    if extension in allow_file_name:
      print(f"檔案型態: {extension}")
      print(f"url: {href}")
      download_img(href, f"{dir_name}/{file_name}")
    
    # print(href)

  # 3. 如果是圖片的話就下載

if __name__ == '__main__':
  main()