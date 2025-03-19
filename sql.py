import sqlite3

def creatorTableSql():
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Gamer (
                       id INTEGER PRIMARY KEY,
                       username TEXT NOT NULL,
                       score INTEGER
                       )
                   ''')
    connection.commit()
    connection.close()
def insert(username,score):
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Gamer (username, score) VALUES (?, ?)', (username, score))
    connection.commit()
    connection.close()
def top5():
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT username, score FROM Gamer ORDER BY score DESC')
    results = cursor.fetchmany(5)
    connection.close()
    return results
