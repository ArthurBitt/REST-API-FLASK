import pytest
from application import create_app


class TestApplication:

    @pytest.fixture()
    def client(self):
        app = create_app('config.MockConfig')

        yield app.test_client()

    @pytest.fixture()
    def valid_user(self):
        return {
            'name': 'John',
            'last_name': 'Doe',
            'cpf': '10712504001',
            'email': 'emailteste@ex.com',
            'birth_date': '1990-01-01'
        }

    @pytest.fixture()
    def invalid_user(self):
        return {
            'name': 'John',
            'last_name': 'Doe',
            'cpf': '12345678910',
            'email': 'emailteste@ex.com',
            'birth_date': '1990-01-01'
        }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_user(self, client, valid_user, invalid_user):
        response = client.post('/user', json=valid_user)
        print(response)
        assert response.status_code == 201
        assert b'successfully' in response.data

        response = client.post('/user', json=invalid_user)
        print(response)
        assert response.status_code == 400
        assert b'Invalid CPF' in response.data

    def test_get_user(self, client, valid_user, invalid_user):
        response = client.get('/user/%s' % valid_user.get('cpf'))
        assert response.status_code == 200
        assert response.json.get('name').lower() == 'john'
        assert response.json.get('cpf').lower() == '10712504001'
        assert response.json.get('last_name').lower() == 'doe'
        assert response.json.get('email').lower() == 'emailteste@ex.com'

        response = client.get('/user/%s' % invalid_user.get('cpf'))
        assert response.status_code == 404
        assert b'User not found' in response.data
