import csv
import random
import sqlite3

conn = sqlite3.connect('movie_tmdb.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = conn.cursor()

# drop the tables - use this order due to foreign keys - so that we can rerun the file as needed without repeating values

conn.execute('DROP TABLE IF EXISTS popular')
conn.execute('DROP TABLE IF EXISTS overview')
conn.execute('DROP TABLE IF EXISTS genres')
conn.execute('DROP TABLE IF EXISTS itemDetails')
print('Table drop successfully!')

# create the tables again - create them in reverse order of deleting due to foreign keys

# popular table
conn.execute(
    'CREATE TABLE popular(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,original_lang TEXT,popularity REAL,vote_count INTEGER,vote_average REAL)')
print('popular table create successfully!')

# overview table
conn.execute('CREATE TABLE overview(id INTEGER PRIMARY KEY AUTOINCREMENT,movieView TEXT)')
print('overview table create successfully!')

# genres table
conn.execute('CREATE TABLE genres (id INTEGER PRIMARY KEY AUTOINCREMENT,movieGenres TEXT)')
print('genres table create successfully!')

# itemDetails table
conn.execute(
    'CREATE TABLE itemDetails(id INTEGER PRIMARY KEY AUTOINCREMENT,popular_id INTEGER, overview_id INTEGER, genres_id INTEGER,  FOREIGN KEY(popular_id) REFERENCES popular(id), FOREIGN KEY(overview_id) REFERENCES overview(id), FOREIGN KEY(genres_id) REFERENCES genres(id))')
print('popular table create successfully!')

# read popular CSV files and input the data to databases
with open('movies_tmdb_popular.csv', newline='')as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)  # skip the header line
    for row in reader:
        title = row[0]
        original_lang = row[1]
        popularity = float(row[2])
        vote_count = int(row[3])
        vote_average = float(row[4])
        cur.execute('INSERT INTO popular VALUES(NULL,?,?,?,?,?)',
                    (title, original_lang, popularity, vote_count, vote_average))
        conn.commit()
print('popular data list input successfully')

# read overview CSV files and input the data to databases
with open('movies_tmdb_overview.csv', newline='')as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)  # skip the header line
    for row in reader:
        movieView = row[0]
        cur.execute('INSERT INTO overview VALUES(NULL,?)', [movieView])
        conn.commit()
print('overview data list input successfully')

# read genres CSV files and input the data to databases
with open('movies_tmdb_genres.csv', newline='')as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)  # skip the header line
    for row in reader:
        movieGenres = row[1]
        cur.execute('INSERT INTO genres VALUES(NULL,?)', [movieGenres])
        conn.commit()
print('genres data list input successfully')

# attach itemDetails to popular,overview and genres
cur.execute('select * from popular')
populars = cur.fetchall()
rowCount = len(populars)

cur.execute('select * from overview')
overviews = cur.fetchall()

cur.execute('select * from genres')
genress = cur.fetchall()

for i in range(rowCount):
    print(i)
    popular_id = populars[i][0]
    overview_id = overviews[i][0]
    genres_id = genress[random.randint(0, 18)][0]
    cur.execute('INSERT INTO itemDetails VALUES(NULL,?,?,?)', (popular_id, overview_id, genres_id))
    conn.commit()
