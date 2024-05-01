import requests
from bs4 import BeautifulSoup

def fetch_data(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  movies = soup.find_all('section', class_='infoArea')
  for movie in movies:
    name = movie.find('a')
    print(name.text)
  


url = 'https://www.vscinemas.com.tw/vsweb/film/index.aspx'

fetch_data(url)