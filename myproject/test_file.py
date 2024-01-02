import requests
import json

###########################################################################################
#test merken
def test_post_merk():
    response = requests.post("http://localhost:8000/merken/", json={"name": "test_merk"})
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["name"]) == str
    assert response_dictionary["name"] == "test_merk"
    assert type(response_dictionary["id"]) == int
    assert type(response_dictionary["accesoires"]) == list

def test_get_merken():
    response = requests.get("http://localhost:8000/merken/")
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    print(response_dictionary)
    print( type(response_dictionary[0]))
    assert type(response_dictionary) == list
    assert type(response_dictionary[0]) == dict
    assert type(response_dictionary[0]["name"]) == str
    assert type(response_dictionary[0]["id"]) == int
    assert type(response_dictionary[0]["accesoires"]) == list

def test_put_merk():
    response = requests.put("http://localhost:8000/merken/1", json={"name": "test_merk2"})
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["name"]) == str
    assert response_dictionary["name"] == "test_merk2"
    assert type(response_dictionary["id"]) == int
    assert type(response_dictionary["accesoires"]) == list

def test_get_merk_by_id():
    response = requests.get("http://localhost:8000/merken/1")
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["name"]) == str
    assert response_dictionary["name"] == "test_merk2"
    assert type(response_dictionary["id"]) == int
    assert response_dictionary["id"] == 1
    assert type(response_dictionary["accesoires"]) == list

###########################################################################################
#test keyboards
def test_post_keyboard():
    response = requests.post("http://localhost:8000/keyboards/?merk_id=1", json={"naam": "test_keyboard", "is_wireless": True})
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["naam"]) == str
    assert response_dictionary["naam"] == "test_keyboard"
    assert type(response_dictionary["id"]) == int
    assert type(response_dictionary["is_wireless"]) == bool
    assert type(response_dictionary["merk_owner_id"]) == int
    assert type(response_dictionary["switches_owner"]) == list

def test_get_keyboards():
    response = requests.get("http://localhost:8000/keyboards/")
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary) == list
    assert type(response_dictionary[0]) == dict
    assert type(response_dictionary[0]["naam"]) == str
    assert type(response_dictionary[0]["id"]) == int
    assert type(response_dictionary[0]["is_wireless"]) == bool
    assert type(response_dictionary[0]["merk_owner_id"]) == int
    assert type(response_dictionary[0]["switches_owner"]) == list

def test_get_keyboard_by_id():
    response = requests.get("http://localhost:8000/keyboards/1")
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["naam"]) == str
    assert type(response_dictionary["id"]) == int
    assert type(response_dictionary["is_wireless"]) == bool
    assert type(response_dictionary["merk_owner_id"]) == int
    assert type(response_dictionary["switches_owner"]) == list


###########################################################################################
#test switches
def test_post_switch():
    response = requests.post("http://localhost:8000/switches/?keyboard_id=1", json={"name": "test_switch", "type": "test_type"})
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["name"]) == str
    assert response_dictionary["name"] == "test_switch"
    assert type(response_dictionary["id"]) == int
    assert type(response_dictionary["type"]) == str
    assert type(response_dictionary["keyboard_id"]) == int

def test_get_switches():
    response = requests.get("http://localhost:8000/switches/")
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary) == list
    assert type(response_dictionary[0]) == dict
    assert type(response_dictionary[0]["name"]) == str
    assert type(response_dictionary[0]["id"]) == int
    assert type(response_dictionary[0]["type"]) == str
    assert type(response_dictionary[0]["keyboard_id"]) == int

def test_get_switch_by_id():
    response = requests.get("http://localhost:8000/switches/1")
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["name"]) == str
    assert type(response_dictionary["id"]) == int
    assert type(response_dictionary["type"]) == str
    assert type(response_dictionary["keyboard_id"]) == int




###########################################################################################
#test users + token

def test_post_user():
    response = requests.post("http://localhost:8000/users/", json={"email": "test@test2", "password": "test"})
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["email"]) == str
    assert response_dictionary["email"] == "test@test2"
    assert type(response_dictionary["id"]) == int
    assert type(response_dictionary["is_active"]) == bool



def test_token_users():
    headers = {
"accept": "application/json",
"Content-Type": "application/x-www-form-urlencoded"
}

    # Account 'test@test.be' with password 'test' has already been pre-made, either manually or with another requests.post
    request_data = {
        "client_id": "",
        "client_secret": "",
        "scope": "",
        "grant_type": "",
        "refresh_token": "",
        "username": "test@test2",
        "password": "test"
    }
    tokenrequest = requests.post("http://localhost:8000/token", data=request_data, headers=headers)
    assert tokenrequest.status_code == 200
    assert type(tokenrequest.text) == str
    assert type(json.loads(tokenrequest.text)) == dict
    assert type(json.loads(tokenrequest.text)['access_token']) == str
    assert type(json.loads(tokenrequest.text)['token_type']) == str
    assert json.loads(tokenrequest.text)['token_type'] == 'bearer'

    # Printing the information for debugging and illustration purposes
    print(tokenrequest.text)
    # Extracting the token that came with the response
    token = json.loads(tokenrequest.text)['access_token']

    # Using the token in the headers of a secured endpoint
    headerswithtoken = {
    "accept" : "application/json",
    "Authorization": f'Bearer {token}'
    }
    response_me = requests.get("http://localhost:8000/users/me", headers=headerswithtoken)
    assert response_me.status_code == 200
    response_dictionary = json.loads(response_me.text)
    assert type(response_dictionary["email"]) == str
    assert response_dictionary["email"] == "test@test2"
    assert type(response_dictionary["id"]) == int
    assert response_dictionary["id"] == 1
    assert type(response_dictionary["is_active"]) == bool

    response_users = requests.get("http://localhost:8000/users/", headers=headerswithtoken)
    assert response_users.status_code == 200
    response_dictionary = json.loads(response_users.text)
    assert type(response_dictionary) == list
    assert type(response_dictionary[0]) == dict
    assert type(response_dictionary[0]["email"]) == str
    assert type(response_dictionary[0]["id"]) == int
    assert type(response_dictionary[0]["is_active"]) == bool

    response_user = requests.get("http://localhost:8000/users/1", headers=headerswithtoken)
    assert response_user.status_code == 200
    response_dictionary = json.loads(response_user.text)
    assert type(response_dictionary["email"]) == str
    assert response_dictionary["email"] == "test@test2"
    assert type(response_dictionary["id"]) == int
    assert response_dictionary["id"] == 1
    assert type(response_dictionary["is_active"]) == bool

def test_delete_user():
    response = requests.delete("http://localhost:8000/users/1")
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["email"]) == str
    assert response_dictionary["email"] == "test@test2"
    assert type(response_dictionary["id"]) == int
    assert response_dictionary["id"] == 1
    assert type(response_dictionary["is_active"]) == bool

###########################################################################################
#delete switches
def test_delete_switch():
    response = requests.delete("http://localhost:8000/switches/1")
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["name"]) == str
    assert response_dictionary["name"] == "test_switch"
    assert type(response_dictionary["id"]) == int
    assert response_dictionary["id"] == 1
    assert type(response_dictionary["type"]) == str
    assert type(response_dictionary["keyboard_id"]) == int
###########################################################################################
#delete keyboards
def test_delete_keyboard():
    response = requests.delete("http://localhost:8000/keyboards/1")
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["naam"]) == str
    assert response_dictionary["naam"] == "test_keyboard"
    assert type(response_dictionary["id"]) == int
    assert response_dictionary["id"] == 1
    assert type(response_dictionary["is_wireless"]) == bool
    assert type(response_dictionary["merk_owner_id"]) == int
    assert type(response_dictionary["switches_owner"]) == list

###########################################################################################
#delete merken
def test_delete_merk():
    response = requests.delete("http://localhost:8000/merken/1")
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["name"]) == str
    assert response_dictionary["name"] == "test_merk2"
    assert type(response_dictionary["id"]) == int
    assert response_dictionary["id"] == 1
    assert type(response_dictionary["accesoires"]) == list

###########################################################################################
