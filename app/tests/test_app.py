import app

def test_home():
    assert app.home() == "Hello from CI/CD Pipeline!"

def test_health():
    response = app.health()
    assert response[0] == "OK"
    assert response[1] == 200

