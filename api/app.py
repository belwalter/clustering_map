from flask import Flask
from flask import render_template, jsonify, request, redirect, url_for
from connectiondb import get_restaurants



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Retorna la pagina index."""
    return render_template('/index.html')

@app.route('/restaurants')
def restaurants():
    lugares = get_restaurants()
    return render_template('/restaurants.html', restaurants=lugares)

if __name__ == '__main__':
    app.run(host='web-clustering', port='5000', debug=True)