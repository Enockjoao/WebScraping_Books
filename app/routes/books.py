from flask import Blueprint, jsonify
import pandas as pd
from app.db.connection import engine

books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['GET'])
def get_books():
    df = pd.read_sql('SELECT * FROM Books', con=engine)
    return jsonify(df.to_dict(orient='records'))