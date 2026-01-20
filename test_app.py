from main import app

def test_home():
    # Indent the function body (4 spaces)
    client = app.test_client()
    response = client.get("/")
    
    assert response.status_code == 200
    assert b"Hello from Argo CD" in response.data