def test_get_recipelist_renders(client):
    #page loads and renders recipelist
    response = client.get('/recipelist')
    assert b'Your entered values' in response.data

def test_post_recipelist_gives_data(client):
    #page loads and handles variables
    response = client.post('/recipelist', data={'kcal':20, 'carbs':30, 'protein':22, 'fat':7})
    assert response is not None