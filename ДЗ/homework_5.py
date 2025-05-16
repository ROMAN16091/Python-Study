import sqlite3
from bs4 import BeautifulSoup
import requests

conn = sqlite3.connect('iphones_info.db')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS phones_info
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
model TEXT,
price TEXT,
disc_price TEXT,
reviews_count TEXT,
model_link TEXT)
""")

url = 'https://rozetka.com.ua/ua/mobile-phones/c80003/producer=apple/'
cont = requests.get(url).text
soup = BeautifulSoup(cont, 'lxml')
models = soup.find_all('a', class_='tile-image-host')
prices = soup.find_all('div', class_ = 'old-price mb-1')
disc_prices = soup.find_all('div', class_ = 'price color-red')
reviews_counts = soup.find_all('span', class_ = 'rating-block-content')
links = soup.find_all('a', class_ = 'tile-image-host')
for model, price, disc_price, review, link in zip(models , prices, disc_prices, reviews_counts, links):
    model_name = model.get('title')
    model_price = price.text.replace('\xa0', ' ')
    model_disc_price = disc_price.text.replace('\xa0', ' ')
    reviews_count = review.text.strip()
    phone_link = link.get('href')
    cur.execute('INSERT INTO phones_info (model, price, disc_price, reviews_count, model_link) VALUES (?, ?, ?, ?, ?)',
                (model_name, model_price, model_disc_price, reviews_count, phone_link))

conn.commit()
conn.close()