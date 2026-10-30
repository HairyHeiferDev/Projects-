import sqlite3
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()


def add_movie():

    cursor.execute("INSERT INTO movies(name,date,genre,watched,rating,id) VALUES (?,?,?,?,?,?)")


def remove_movie():

    cursor.execute




def update_movie():
    cursor.execute
    
    
    
    
        
    
