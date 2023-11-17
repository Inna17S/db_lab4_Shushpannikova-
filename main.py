import psycopg2

username = 'Inna'
password = '111'
database = 'Inna_DB_4'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT Genre.genre_name, COUNT(Genre.genre_name) AS track_count
FROM SongsGenre
JOIN Genre ON SongsGenre.GenreID = Genre.GenreID
GROUP BY Genre.genre_name;
'''

query_2 = '''SELECT Chart.position, Songs.energy
FROM Chart
JOIN Songs ON Chart.Song_ID = Songs.Song_ID;
'''
query_3 = '''SELECT Chart.position, Songs.duration_ms
FROM Chart
JOIN Songs ON Chart.Song_ID = Songs.Song_ID;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:

    print ("Database opened successfully")
    cur = conn.cursor()
    print('1.  \n')

    cur.execute(query_1)

    for row in cur:
        print(row)


    cur = conn.cursor()
    print('\n 2.  \n')

    cur.execute(query_2)

    for row in cur:
        print(row)


    cur = conn.cursor()
    print('\n 3.  \n')

    cur.execute(query_3)

    for row in cur:
        print(row)