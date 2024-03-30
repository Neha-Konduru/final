import unittest
import json
from app import create_app
from database.models import  db, Models

class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        self.database_name = "capstone_test"
        self.database_path = "postgresql://{}/{}".format('konduruneha:testpass@localhost:5432', self.database_name)
        self.app = create_app(test_config={'SQLALCHEMY_DATABASE_URI': self.database_path, 'SQLALCHEMY_TRACK_MODIFICATIONS': False})
        self.client = self.app.test_client

        # binds the app to the current context
        with self.app.app_context():
            Models.setup_db(self.app, self.database_path)
            # create all tables
            db.create_all()


    #Method to get tokens for different roles
    def get_token(self, role):
        if role == 'casting_assistant':
            return 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpfMThZTmMyWk51TEx2bWdObXlRZCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQ5OTkudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY1YjQ5OTllMGJhZjkxNGJkZmZmODNhNCIsImF1ZCI6ImNvZmZlZSIsImlhdCI6MTcxMTc4MjY3MSwiZXhwIjoxNzExNzg5ODcxLCJzY29wZSI6IiIsImF6cCI6ImRMVEhJRUJKV3dBYXo0ckE5MXUwSmpQcU5BaFRRRU05IiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.W2RLn3-YG2G15oGAZ8nXtd5w3g-G9ZQm4Fn64RFbuLmxTbbrtNhPKEJ7yGNnmjB1YSdcqA-s0znaA8d9EMHlwX-x6HYUvyJ-j6ohNhjp03TNXFhiOWrxefdtnftW-kx6vMRRU4pr7k6WIs5IyioYehLTCycSNdV9rQ884Tx5blE-4uZwpJouL4EA6F61ujB2uNOMCuZZUcCNlq6p3oaAyC4ME6n37ZNuxmQSdfAaunJjHvI96V1FwxQpLoXs9fvFyY4LywzjiBAoCDw3PB0YWhZQkYxb1bfS1Pu-_hRv8A1oK5mFHHJzP7JJCm-T0bYdU8J_jvo-b1GX2L_4qksuqg'
        elif role == 'casting_director':
            return 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpfMThZTmMyWk51TEx2bWdObXlRZCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQ5OTkudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY1YjY5NmZmMGYwNjcxYWFmOTZjYWNmOSIsImF1ZCI6ImNvZmZlZSIsImlhdCI6MTcxMTc4MjIyNSwiZXhwIjoxNzExNzg5NDI1LCJzY29wZSI6IiIsImF6cCI6ImRMVEhJRUJKV3dBYXo0ckE5MXUwSmpQcU5BaFRRRU05IiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.mu8QMcQoUeiriTaZlcE2Tb0ZpsBJmcf-mYAey-va4jsfj3op6200jNuWlLt82lUaw9ZBv4njjK3-qF8ESWHhmoH2JK-CyDhDXgNa1-v2uL90PqXkRbMbpQd0P5iIjdnxWXS-J4yk6I_zEQzLoQyND4xjpAS6F7ZHXKKubTbRQXjgctzwWFUV9HLLoRYqvVo2VCtgunIWOwchgtOs6JKbilVvV-K3gCMV4J6W5Au4smWl3qbaKqdF5WL27r64oANBPy2Oe6ieWlmnG2Pml3_SG4H6aWZ9-c7ps43G7homjJJDUXouLCEAYL43OAxBhGJvQ9sOWhjxbw6abv9-wWLkyg'
        elif role == 'executive_producer':
            return 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpfMThZTmMyWk51TEx2bWdObXlRZCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQ5OTkudXMuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEzNDMxOTM2NDQ0NTAzODIxNjU4IiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNzExNzgyMDc3LCJleHAiOjE3MTE3ODkyNzcsInNjb3BlIjoiIiwiYXpwIjoiZExUSElFQkpXd0FhejRyQTkxdTBKalBxTkFoVFFFTTkiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.LWtA_lAxC7fAYYSSNqz1iftni5Q_eZhOTUeSk5uyN2YXg8uYaOTauwb-XyU4TzzaxboCPrBvkzVZ_b8obTi6CRVOyDFyE7NJlxL5Irb3n-ohbopFiLW4Zda_QXqQ4vP0R_DMgPec7K-ffZmjpivtCXcjKkowQATYrAQJ7__sNZS7GxVF_p2Z5lGoUxH0U4CXUH4RcajAbOKLjpqFRYvxYsHotEnQeSB9cyVS9bANkVwCsjtGeIFrWs-35oKvOFHlwnvpj8fTPNwZlolCXwD02UMj7jDfx_xsdrpPkhkEmkqu2sFMWUDPYPRkwkbO8caSMYTFLvyH9NnmGqvwmXnVCQ'
        else:
            return None

    def test_casting_assistant_get_actors(self):
        token = self.get_token('casting_assistant')
        response = self.client().get('/actors', headers={'Authorization': f'Bearer {token}'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actors']) > 0)

    
    def test_casting_assistant_delete_actor_failure(self):
        token = self.get_token('casting_assistant')
        response = self.client().delete('/actors/1000', headers={'Authorization': f'Bearer {token}'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403)
        self.assertFalse(data['success'])

    def test_casting_assistant_add_actor_failure(self):
        token = self.get_token('casting_assistant')
        response = self.client().post('/actors', json={}, headers={'Authorization': f'Bearer {token}'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403)
        self.assertFalse(data['success'])

    def test_casting_director_delete_actor(self):
        token = self.get_token('casting_director')
        actor_id = Models.Actors.query.first().id
        response = self.client().delete(f'/actors/{actor_id}', headers={'Authorization': f'Bearer {token}'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

    def test_casting_director_add_actor(self):
        token = self.get_token('casting_director')
        response = self.client().post('/actors', json={'name': 'John', 'age': 30, 'gender': 'Male'}, headers={'Authorization': f'Bearer {token}'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

    def test_casting_director_get_movies_failure(self):
        token = self.get_token('casting_director')
        response = self.client().get('/movies', headers={'Authorization': f'Bearer {token}'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

    def test_executive_producer_delete_movie(self):
        token = self.get_token('executive_producer')
        movie_id = Models.Movies.query.first().id
        response = self.client().delete(f'/movies/{movie_id}', headers={'Authorization': f'Bearer {token}'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

    def test_executive_producer_add_movie(self):
        token = self.get_token('executive_producer')
        response = self.client().post('/movies', json={'title': 'New Movie', 'release_date': '2024-03-30'}, headers={'Authorization': f'Bearer {token}'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

    def test_executive_producer_update_actor_failure(self):
        token = self.get_token('executive_producer')
        actor_id = Models.Actors.query.first().id
        response = self.client().patch(f'/actors/{actor_id}', json={'name': 'New Name'}, headers={'Authorization': f'Bearer {token}'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_actors_no_data(self):
        res = self.client().get('/actors', headers={'Authorization': f'Bearer invalid'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 500)
        self.assertFalse(data['success'])

    def test_get_movies_no_data(self):
        res = self.client().get('/movies',headers={'Authorization': f'Bearer invalid'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 500)
        self.assertFalse(data['success'])

    def test_delete_nonexistent_actor(self):
        token = self.get_token('executive_producer')
        res = self.client().delete('/actors/invalid', headers={'Authorization': f'Bearer {token}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])


    def test_delete_nonexistent_movie(self):
        token = self.get_token('executive_producer')
        res = self.client().delete('/movies/1000', headers={'Authorization': f'Bearer {token}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_update_actor_invalid_id(self):
        token = self.get_token('executive_producer')
        actor_data = {'name': 'Updated Test Actor'}
        res = self.client().patch('/actors/invalid_id', json=actor_data, headers={'Authorization': f'Bearer {token}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_update_movie_invalid_id(self):
        token = self.get_token('executive_producer')
        movie_data = {'title': 'Updated Test Movie'}
        res = self.client().patch('/movies/invalid_id', json=movie_data, headers={'Authorization': f'Bearer {token}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_add_actor_missing_data(self):
        token = self.get_token('executive_producer')
        actor_data = {}  
        res = self.client().post('/actors', json=actor_data, headers={'Authorization': f'Bearer {token}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])

    def test_add_movie_missing_data(self):
        token = self.get_token('executive_producer')
        movie_data = {} 
        res = self.client().post('/movies', json=movie_data, headers={'Authorization': f'Bearer {token}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])

if __name__ == "__main__":
    unittest.main()

