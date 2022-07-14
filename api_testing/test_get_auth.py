import requests
import jsonpath

url = 'https://httpbin.org/basic-auth/andrey/heihei'


response = requests.get(url,
            auth=('andrey', 'heihei')
            )

def test_auth_code():
    assert response.status_code == 200, "!!!Incorrect code response!!!"
    print('\nResponse code =', response.status_code)

def test_auth_body():
    assert response.json() == \
           {
               "authenticated": True,
               "user": "andrey"
           }, "!!!Incorrect body response!!!"
    print('\nBody response is correct')

def test_spec_body():
    response_json = response.json()
    auth = jsonpath.jsonpath(response_json, "authenticated")
    assert auth == [True], "!!!Authorization is faile!!!"
    print('\nUser is authorizated')