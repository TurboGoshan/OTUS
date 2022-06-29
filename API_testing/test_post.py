import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"

# Open save file on PC
file = open("C:\\otus-qa-course\\user.json", "r")
# Read json file
json_input = file.read()
# Transfer file to json
request_json = json.loads(json_input)
# Make post method
response = requests.post(url, request_json)


# Compare actual and expected codes
def test_post_code():
    assert response.status_code == 201
    print("\n", response.status_code)


# Compare special header value
def test_post_special_value():
    assert response.headers.get('connection') == 'keep-alive', "!!!Incorrect special value in header!!!"
    print(response.headers.get('connection'))


# Compare special values from response
def test_post_response():
    # Transfer text response to json
    response_json = response.json()
    # Pick the name parameter
    name = jsonpath.jsonpath(response_json, "name")
    assert name == ['morpheusup'], "!!!Incorrect special value in response!!!"
    print(name)
