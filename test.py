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
            return 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpfMThZTmMyWk51TEx2bWdObXlRZCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQ5OTkudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY1YjQ5OTllMGJhZjkxNGJkZmZmODNhNCIsImF1ZCI6ImNvZmZlZSIsImlhdCI6MTcxMTc5MjkxMCwiZXhwIjoxNzExODAwMTEwLCJzY29wZSI6IiIsImF6cCI6ImRMVEhJRUJKV3dBYXo0ckE5MXUwSmpQcU5BaFRRRU05IiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.QP8zdLwM_kpJnyyBt5Et1TSKEK8EUISonwJ4OXYYjfuTsMf8X_5UZUcbkSwouzrb87r4y1ctGLjkzdthJg0QbgwUcKH_yjqJuD_Aux6rt6nVs1d9FafFdxw7c-VxP72kQy64Kn3F4WesAxi8Oo4YzdD2LNiFJiYFZLBha5Gt6RE1q2b-W24tUIioEflf_TIh8ksPQyM0hz5r2F7XovokLYG6tLDS-w8UQo4GSmE_j7nvAhK_tcWuJBkpO12WYy4lSNwG9wHkjXxFw0StmKKSO_0uL5KfrACLrXryaWuFpyGJcfYV1tq2ilNB8ar24FUfipsq7lhQxU50j18FUMmWPw'
        elif role == 'casting_director':
            return 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpfMThZTmMyWk51TEx2bWdObXlRZCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQ5OTkudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY1YjY5NmZmMGYwNjcxYWFmOTZjYWNmOSIsImF1ZCI6ImNvZmZlZSIsImlhdCI6MTcxMTc5Mjg1OCwiZXhwIjoxNzExODAwMDU4LCJzY29wZSI6IiIsImF6cCI6ImRMVEhJRUJKV3dBYXo0ckE5MXUwSmpQcU5BaFRRRU05IiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.b0p_Rv6I4sJ69N_oiDRK1SzHdLNJSN9g8gcWVXJbJgtiVtoce32DvKvEZ1Wijfg3FBDdnAOLOxGTtnQLs3SsQ_vXAsKD3Q0h1kNL7uUIbJ_aMwvRtcNspiKIu_7Ziss6N6tJZ1JDIW70Ynm-1DQN5iOBFbAaV5ZrJ_H4RFm6UngQPC6ocYZ7VsJ5QIJxcr7qIWmwtOXlTU6Zqo3xdj5hhkAqnqA4v4M0rC5eASFpL11UV2MAMMPvnRm--qXI2x5LtOrI_50m5I0FQ0bEZBR6wx3CS7MBlfOqu9G_r-GmKIyLCQUJ_DO2GFD2ERTk_HqbNPzM1psGNGkgceWsWi9mWQ'
        elif role == 'executive_producer':
            return 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpfMThZTmMyWk51TEx2bWdObXlRZCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQ5OTkudXMuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEzNDMxOTM2NDQ0NTAzODIxNjU4IiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNzExNzkyOTU3LCJleHAiOjE3MTE4MDAxNTcsInNjb3BlIjoiIiwiYXpwIjoiZExUSElFQkpXd0FhejRyQTkxdTBKalBxTkFoVFFFTTkiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.X4KRHhyIE4dTuVlrGz9oMlpcboNGzDrtXLaNDZx6UlixB7Xr_Nc2UJ2mBdFvBfDhsMGDlVRgQ0b6qUUIRrF2o2dicC99pPO5Xk7a5VHB7pRCQlcFYC-Bw1g_DyShaF0eM2Xd3T4VuRy2A7cXtZXfVz5joBDPvAoGdP8hEs8E5rMD_KI-vUNzboU3X-05fDTuEplPmIG93gomLXQcasBqkMUjqn0acVX7VvSn__LSRu589QdlJW2jdPxeN3qzqK4Eq1PyZoF56bG0Fv_srZ0AaHHSEBFdf-brUEoQYUfNMdgULF4EawrKPiwFcoXMkcJh_dQ7UKx2QqLAwpLxb8Dp_A'
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

