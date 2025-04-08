from flask import Blueprint, jsonify
from app.scraper.book_scraping import BookScraping

scrape_bp = Blueprint('scrape', __name__, url_prefix='/scrape')

@scrape_bp.route('/', methods=['POST'])
def scrape_books():
    try:
        urls = [
            "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
            "https://books.toscrape.com/catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html",
            "https://books.toscrape.com/catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html"        
        ]

        scraper = BookScraping(urls)
        scraper.run()
        return jsonify({"message": "Raspagem concluída com sucesso!"}), 200

    except Exception as e:
        return jsonify({'erro': str(e)}), 500    
