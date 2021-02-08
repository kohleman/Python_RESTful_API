import unittest
from main import app


class BoardgamesApiTest(unittest.TestCase):
    def setUp(self):
        # 1. ARRANGE
        self.app = app.test_client()
        # initialize app with first boardgame
        self.app.post('/boardgames', json={
            "name": "Wingspan",
            "designer": "Elizabeth Hargrave",
            "playing_time": "60 Min",
            "rating": 8.1,
            "id": "1",
            "expansions": [{"name": "European Expansion", "rating": 8.5}]
        })

    def test_get_boardgame_by_id(self):
        # 2. ACT
        response = self.app.get('/boardgames/1')
        # 3. ASSERT
        self.assertEqual('200 OK', response.status)
        self.assertEqual('Wingspan', response.json['name'])

    def test_get_boardgame_for_unknwon_id(self):
        # 2. ACT
        response = self.app.get('/boardgames/2')
        # 3. ASSERT
        self.assertEqual('404 NOT FOUND', response.status)
        self.assertTrue("Boardgame 2 not found." in response.json['message'])

    def test_delete_boardgame_by_id(self):
        # 2. ACT
        response = self.app.delete('/boardgames/1')
        # 3. ASSERT
        self.assertEqual('204 NO CONTENT', response.status)
        response = self.app.get('/boardgames')
        self.assertEqual(0, len(response.json))

    def test_post_new_boardgame(self):
        # 2. ACT
        response = self.app.post('/boardgames', json={
            "name": "King of Tokyo",
            "designer": "Richard Garfield",
            "playing_time": "30 Min",
            "rating": 7.2,
            "id": "2",
            "expansions": []
        })
        # 3. ASSERT
        self.assertEqual('201 CREATED', response.status)
        self.assertEqual('King of Tokyo', response.json['name'])
