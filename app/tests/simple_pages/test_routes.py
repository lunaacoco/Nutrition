def test_index_success(client):
    #page loads
    response = client.get('/')
    assert response.status_code == 200

#first test: failing test with different text
#second test: check if client gets 'welcome' when requesting the html 
def test_index_content(client):
    #returns welcome
    response = client.get('/')
    assert b'welcome' in response.data