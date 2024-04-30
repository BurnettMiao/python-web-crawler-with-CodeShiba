import requests
from bs4 import BeautifulSoup

def fetch_data(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  movies = soup.find_all('div', class_='poster-info')
  for movie in movies:
    name = movie.find('div', class_='title')
    name = name.a.text.strip()
    engName = movie.find('p', class_='show-for-large')
    engName = engName.text.strip()
    


url = 'https://www.ambassador.com.tw/home/MovieList?Type=1'

fetch_data(url)