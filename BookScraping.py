import requests as r
from bs4 import BeautifulSoup as bs
import pandas as pd
url='https://books.toscrape.com/'
response = r.get(url)
soup=bs(response.content,'html.parser')
book_list = soup.find_all('article', class_='product_pod')
btitles=[]
bprices=[]
for book in book_list:
    title = book.h3.a['title']
    btitles.append(title)
    price = book.find('p', class_='price_color').text.strip()
    bprices.append(price)
datframe_pd=pd.DataFrame({"title":btitles,"prices":bprices},index=range(1,len(btitles)+1))
print(datframe_pd)