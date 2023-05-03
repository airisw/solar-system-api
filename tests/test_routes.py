def test_get_all_planets_return_empty_list_when_db_is_empty(client):
    response = client.get("/planets")

    assert response.status_code == 200 
    assert response.get_json() == []

def test_get_one_planet_return_planet(client, one_planet):
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()

    assert response.status_code == 200 
    assert response_body["name"] == one_planet.name
    assert response_body["description"] == one_planet.description
    assert response_body["orbital_period"] == one_planet.orbital_period

def test_get_one_planet_return_error(client):
    response = client.get("/planets/1")

    assert response.status_code == 404

def test_get_all_planets_return_db(client, two_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200 
    assert response_body[0]["name"] == two_planets[0]["name"]
    assert response_body[0]["description"] == two_planets[0]["description"]
    assert response_body[0]["orbital_period"] == two_planets[0]["orbital_period"]
    assert response_body[1]["name"] == two_planets[1]["name"]
    assert response_body[1]["description"] == two_planets[1]["description"]
    assert response_body[1]["orbital_period"] == two_planets[1]["orbital_period"]

def test_post_planet(client):
    EXPECTED_PLANET = {
        "name": "Planet 1",
        "description": "description 1",
        "orbital_period": 10}
    
    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)

    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} successfully created"




