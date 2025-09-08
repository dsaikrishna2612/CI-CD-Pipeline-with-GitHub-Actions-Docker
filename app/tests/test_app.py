import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import home, health

def test_home():
    assert home() == "Hello from CI/CD Pipeline!"

def test_health():
    response = health()
    assert response[0] == "OK"
    assert response[1] == 200
