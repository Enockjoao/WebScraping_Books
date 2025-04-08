from flask import Flask
from flask_cors import CORS
from app.routes.books import books_bp
from app.routes.scraper import scrape_bp
from app.db.connection import engine



def create_app():
    app = Flask(__name__)
    CORS(app)

    from app.routes.books import books_bp
    from app.routes.scraper import scrape_bp

    app.register_blueprint(books_bp)
    app.register_blueprint(scrape_bp)

    @app.route('/')
    def home():
        return {'Mensagem': 'API de Livros funcionando!'}

    return app