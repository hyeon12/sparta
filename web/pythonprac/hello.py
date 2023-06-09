from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.k3deo2l.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

URL = "https://movie.daum.net/ranking/reservation"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

#mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont > strong
movies = soup.select("#mainContent > div > div.box_ranking > ol > li")

for movie in movies:
    title = movie.select_one('.link_txt').text
    rank = movie.select_one('.rank_num').text
    rate = movie.select_one('.txt_grade').text
    if title is not None:	# None이 아닐때만
        doc = {
            'title': title,
            'rank': rank,
            'rate': rate
        }
        db.movies.insert_one(doc)