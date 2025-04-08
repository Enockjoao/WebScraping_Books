import requests
import pandas as pd
from bs4 import BeautifulSoup


class BookScraping:
    def __init__(self, urls):
        self.urls = urls
        self.livros = []


    def fetch_book(self, url):
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
            "Description":description
            
        }


    def run(self):
        for url in self.urls:
            try:
                book = self.fetch_book(url)
                self.livros.append(book)
            except Exception as e:
                print(f"Erro ao processar {url}: (e)")


        df =pd.DataFrame(self.livros)
        df.to_csv("data/save_books.csv", index=False, encoding="utf-8")
        print("✍️ Dados salvos com sucesso em 'save_book.csv'")
     
        from app.db.connection import engine
        df.to_sql('Books', con=engine, if_exists='append', index=False)
        print("✍️ Todos os dados foram salvos no Banco de Dados'")


