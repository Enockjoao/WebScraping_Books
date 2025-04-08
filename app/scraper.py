from bs4 import BeautifulSoup
import requests
import pandas as pd
from sqlalchemy import Column , Integer, String, create_engine
from sqlalchemy.orm import declarative_base , sessionmaker

def BookScraping(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")



    title = soup.select_one("div.product_main h1").text
    price = soup.select_one("p.price_color").text
    availability = soup.select_one("p.instock.availability").text.strip()
    #rating = soup.select_one("p.star_rating Three")["class"][1]
    description_tag = soup.select_one("div#Product_Description ~ p")
    description = description_tag.text if description_tag else "Sem descrição"


    return {
        "Título":title,
        "price":price,
        "availability":availability,
        "Description":description_tag
        
    }

urls = [
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "https://books.toscrape.com/catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html",
    "https://books.toscrape.com/catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html"
        
]
livros = []

for url in urls:
    livro = BookScraping(url)
    livros.append(livro)


df =pd.DataFrame(livros)
df.to_csv("../data/save_book.csv", index=False, encoding="utf-8")
print("Dados salvos com sucesso em 'save_book.csv'")

df = pd.read_csv("../data/save_book.csv")

engine = create_engine('sqlite:///../database/BookingDB.db')

df.to_sql('Books', con=engine, if_exists='append', index='False')

print("Banco de dados Criado com Sucesso em 'BookingDB.db'")

BookScraping(url)

    
