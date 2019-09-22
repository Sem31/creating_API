from flask import Blueprint, jsonify, request
# from model import Movie,db
from run import app
from flask import Flask
import pymysql
from model import mysql

conn = mysql.connect()
cursor = conn.cursor(pymysql.cursors.DictCursor)


@app.route('/add_movie', methods=['POST'])
def add_movie():
    movie_data = request.get_json()
    print(movie_data)
    cursor.execute("insert into Movie values(%s,%s)", (movie_data['title'],movie_data['rating']))
    conn.commit()
    return jsonify(movie_data)

@app.route('/movie')
def movies():
    cursor.execute("SELECT * FROM Movie")
    rows = cursor.fetchall()
    print(rows)

    return jsonify({'movies' : rows})



if __name__ == "__main__":
    app.run(debug=True)