import os
from flask import Flask, request, abort, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from auth.auth import AuthError, requires_auth


from database.models import Models, db


# Set up pagination constant
ACTORS_PER_PAGE = 10
MOVIES_PER_PAGE = 10

# Method for paginating actors
def paginate_actors(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * ACTORS_PER_PAGE
    end = start + ACTORS_PER_PAGE

    actors = [actor.format() for actor in selection]
    current_actors = actors[start:end]

    return current_actors

# Method for paginating movies
def paginate_movies(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * MOVIES_PER_PAGE
    end = start + MOVIES_PER_PAGE

    movies = [movie.format() for movie in selection]
    current_movies = movies[start:end]

    return current_movies

def create_app(test_config=None):
    app = Flask(__name__)
    if test_config:
        app.config.from_mapping(test_config)
    else:
        Models.setup_db(app)

    #CORS, allowing all origins
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    

    # After request decorator to set response headers for CORS
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response
    

    # GET endpoint to fetch all actors
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
            actors = Models.Actors.query.all()
            paginated_actors = paginate_actors(request, actors)

            return jsonify({
                'success': True,
                'actors': paginated_actors,
                'total_actors': len(actors)
            })

    # GET endpoint to fetch all movies
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
            movies = Models.Movies.query.all()
            paginated_movies = paginate_movies(request, movies)

            return jsonify({
                'success': True,
                'movies': paginated_movies,
                'total_movies': len(movies)
            })

    # DELETE endpoint to delete an actor by id
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload,actor_id):
            actor = Models.Actors.query.filter_by(id=actor_id).one_or_none()
            if actor is None:
                abort(404)
            actor.delete()

            return jsonify({
                'success': True,
                'deleted': actor_id
            })

    # DELETE endpoint to delete a movie by id
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload,movie_id):
            movie = Models.Movies.query.filter_by(id=movie_id).one_or_none()
            if movie is None:
                abort(404)
            movie.delete()

            return jsonify({
                'success': True,
                'deleted': movie_id
            })

    # POST endpoint to add a new actor
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actor(payload):
            data = request.get_json()
            name = data.get('name')
            age = data.get('age')
            gender = data.get('gender')

            if not (name and age and gender):
                abort(400)

            actor = Models.Actors(name=name, age=age, gender=gender)
            actor.insert()

            return jsonify({
                'success': True,
                'created': actor.id
            })

    # POST endpoint to add a new movie
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movie(payload):
            data = request.get_json()
            title = data.get('title')
            release_date = data.get('release_date')

            if not (title and release_date):
                abort(400)

            movie = Models.Movies(title=title, release_date=release_date)
            movie.insert()

            return jsonify({
                'success': True,
                'created': movie.id
            })


    # PATCH endpoint to update an actor
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(payload,actor_id):
            actor = Models.Actors.query.filter_by(id=actor_id).one_or_none()
            if actor is None:
                abort(404)

            data = request.get_json()
            if 'name' in data:
                actor.name = data['name']
            if 'age' in data:
                actor.age = data['age']
            if 'gender' in data:
                actor.gender = data['gender']
            
            actor.update()

            return jsonify({
                'success': True,
                'updated': actor.id
            })

    # PATCH endpoint to update a movie
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(payload,movie_id):
            movie = Models.Movies.query.filter_by(id=movie_id).one_or_none()
            if movie is None:
                abort(404)

            data = request.get_json()
            if 'title' in data:
                movie.title = data['title']
            if 'release_date' in data:
                movie.release_date = data['release_date']

            movie.update()

            return jsonify({
                'success': True,
                'updated': movie.id
            })

    # Error handlers
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad request'
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method not allowed'
        }), 405

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unprocessable entity'
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal'
        }), 500
    
    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run()