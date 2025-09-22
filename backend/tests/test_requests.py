import requests

def test_logout_response():
    response = requests.post('http://127.0.0.1:8000/api/v1/accounts/logout')
    assert response.status_code == 204

def test_auth():
    response = requests.get('http://127.0.0.1:8000/api/v1/accounts/my')
    assert response.status_code == 401