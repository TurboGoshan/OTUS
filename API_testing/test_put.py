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
response = requests.put(url, request_json)


# Compare actual and expected codes
def test_post_code():
    assert response.status_code == 200, "!!!INCORRECT CODE!!!"
    print("\n", response.status_code)


# Test some several values from servers response
def test_post_response():
    # Transfer text response to json
    response_json = response.json()
    name = jsonpath.jsonpath(response_json, "name")
    job = jsonpath.jsonpath(response_json, "job")
    assert name == ['morpheusup'], "!!!Incorrect special value in name response!!!"
    assert job == ['leaderup'], "!!!Incorrect special value in job response!!!"
    print(response_json)
