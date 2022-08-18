import os

from flask import Flask, jsonify, render_template, send_file
import sqlite3

template_dir = os.path.abspath('./Front/')
app = Flask(__name__, template_folder=template_dir)


@app.route('/api/health_check', methods=['GET'])
def check_health():
    return jsonify({
        'message': 'OK'
    }), 200


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/images/<image>')
@app.route('/movies/images/<image>')
def get_image(image):
    return send_file(f'Front/images/{image}')


@app.route('/movies/Front/local_dash/<id>/<file>')
def get_dash(id, file):
    return send_file(f'Front/local_dash/{id}/{file}')


@app.route('/movies/<id>')
def movie(id):
    id = int(id)
    if id < 3:
        return render_template(f'movies/1/index.html', id=id)
    elif 2 < id < 5:
        return render_template(f'movies/2/index.html', id=id)
    else:
        return render_template(f'movies/3/index.html', id=id)


@app.route('/api/movies')
def api_movies():
    conn = sqlite3.connect('movies.db')
    movies = list()
    cursor = conn.execute("SELECT id,name,poster_path,score from movies")
    for row in cursor:
        movies.append({'id': row[0], 'name': row[1], 'poster_path': row[2], 'score': row[3]})
    conn.close()
    return jsonify(movies)


@app.route('/api/movies/<id>')
def api_movie_info(id):
    id = int(id)
    conn = sqlite3.connect('movies.db')
    cursor = conn.execute(f"SELECT * from movies where id={id}")
    res = ""
    for row in cursor:
        if id < 3:
            res = {'name': row[1], 'score': row[2], 'director_name': row[3], 'definition': row[4],
                   'poster_path': row[5], 'local_url': row[8]}
        elif 2 < id < 5:
            res = {'name': row[1], 'score': row[2], 'director_name': row[3], 'definition': row[4],
                   'poster_path': row[5], 'dash_url': row[6]}
        else:
            res = {'name': row[1], 'score': row[2], 'director_name': row[3], 'definition': row[4],
                   'poster_path': row[5], 'hls_url': row[7]}
        break
    conn.close()
    return jsonify(res)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
