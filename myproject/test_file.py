import requests
import json

def test_get_merken():
    response = requests.get("http://127.0.0.1:8000/merken/")
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    print(response_dictionary)
    print( type(response_dictionary[0]))
    assert type(response_dictionary) == list
    assert type(response_dictionary[0]) == dict
    assert type(response_dictionary[0]["name"]) == str
    assert type(response_dictionary[0]["id"]) == int
    assert type(response_dictionary[0]["accesoires"]) == list



def test_get_keyboards():
    response = requests.get("http://127.0.0.1:8000/keyboards/")
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary) == list
    assert type(response_dictionary[0]) == dict
    assert type(response_dictionary[0]["naam"]) == str
    assert type(response_dictionary[0]["id"]) == int
    assert type(response_dictionary[0]["is_wireless"]) == bool
    assert type(response_dictionary[0]["merk_owner_id"]) == int
    assert type(response_dictionary[0]["switches_owner"]) == list

def test_get_switches():
    response = requests.get("http://127.0.0.1:8000/switches/")
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary) == list
    assert type(response_dictionary[0]) == dict
    assert type(response_dictionary[0]["name"]) == str
    assert type(response_dictionary[0]["id"]) == int
    assert type(response_dictionary[0]["type"]) == str
    assert type(response_dictionary[0]["keyboard_id"]) == int

test_get_merken()