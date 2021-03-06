import sqlite3

from flask import Flask, g, render_template

app = Flask(__name__)

# load the configuration to smooth database connections
app.config.from_object(__name__)

# database details - to remove some duplication
db_name = 'movie_tmdb.db'


def connect_db():
    conn = sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn.row_factory = sqlite3.Row
    return conn


# When this function is called for the first time, it will create a database connection for the current environment.
# After the call is successful, it will return the established connection.:
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/movie_details')
def movie_rating():
    db = get_db()
    # get results from popular
    cur = db.execute('select * from popular')
    rows = cur.fetchall()
    return render_template('rating_details.html', rows=rows)


@app.route('/genres_details')
def movie_genres():
    db = get_db()
    # get results from genres
    cur = db.execute('select * from genres')
    rows = cur.fetchall()
    return render_template('genres_details.html', rows=rows)


@app.route('/overview_details')
def movie_overview():
    db = get_db()
    # get results from overview
    cur = db.execute('select * from overview')
    rows = cur.fetchall()
    return render_template('overview_details.html', rows=rows)


# if user click number from genres page, that can find this series of movies
@app.route('/same_genres/<id>')
def same_genres(id):
    db = get_db()
    # get results from itemDetails
    cur = db.execute("select * from itemDetails WHERE genres_id=?", [id])
    allGenres = cur.fetchall()
    cur = db.execute('select * from popular')
    popular = cur.fetchall()
    return render_template('same_genres.html', allGenres=allGenres, popular=popular)


# if user click number from overview page, that can check all details of the whole movie
@app.route('/all_details/<id>')
def all_details(id):
    db = get_db()
    # get results from itemDetails
    cur = db.execute("select * from itemDetails WHERE overview_id=?", [id])
    item_order = cur.fetchall()
    # according the id and get results from popular
    popular_id = item_order[0][1]
    cur = db.execute("select * from popular WHERE id=?", [popular_id])
    popular_item = cur.fetchall()

    # according the id and get results from overview
    cur = db.execute("select * from overview WHERE id=?", [id])
    overview_item = cur.fetchall()

    # according the id and get results from genres
    genres_id = item_order[0][3]
    cur = db.execute("select * from genres WHERE id=?", [genres_id])
    genres_item = cur.fetchall()
    return render_template('all_details.html', popular_item=popular_item, overview_item=overview_item, genres_item=genres_item)


if __name__ == '__main__':
    app.run(host='0,0,0,0')
