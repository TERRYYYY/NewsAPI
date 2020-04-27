from flask import render_template
from . import main
from ..requests import get_news,get_article

@main.route('/')
def index():
    trending_news = get_news('trending')

    return render_template('index.html',trending=trending_news)

@main.route('/news/<id>')
def sources(id):
    articles = get_article(id)
    return render_template('articles.html' , name = id , article = article)