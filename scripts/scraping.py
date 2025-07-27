import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
books = soup.find_all('article', class_='product_pod')
data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    data.append({'title': title, 'price': price})
df = pd.DataFrame(data)
print(df)
df.to_csv('DE_E2E\\scripts\\books.csv', index=False)