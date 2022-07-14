import requests

url = "https://reqres.in/api/users/2"


# Compare the actual and expected cods
def test_delete_code():
    response = requests.delete(url)
    assert response.status_code == 204, "!!!Incorrect code!!!"
    print("\n", response.status_code)