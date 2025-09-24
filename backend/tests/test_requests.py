import requests

def test_logout_response():
    response = requests.post('http://127.0.0.1:8000/api/v1/accounts/logout')
    response2 = requests.post('http://127.0.0.1:8000/api/v1/accounts/logout')
    assert response.status_code == 204, (
        "Logout request should be idempotent"
    )
    assert response2.status_code == 204, (
        "Logout request should be idempotent"
    )

def test_auth():
    response = requests.get('http://127.0.0.1:8000/api/v1/accounts/my')
    assert response.status_code == 401, (
        "Auth middleware should working"
    )