import requests
from bs4 import BeautifulSoup

url="https://books.toscrape.com/" 
response=requests.get(url)
print(response.status_code)

soup=BeautifulSoup(response.text,"html.parser")
print(soup.title.text)

books=soup.find_all("h3")
for book in books:
    print(book.a["title"])