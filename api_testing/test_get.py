import requests
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"
response = requests.get(url)


# Compare code between actual and expected
def test_get_code():
    assert response.status_code == 200, "!!!Incorrect code response!!!"
    print("\nresponse code =", response.status_code)

# Compare body between actual and expected
def test_get_body():
    assert response.json() == \
           {
               "page": 2,
               "per_page": 6,
               "total": 12,
               "total_pages": 2,
               "data": [
                   {
                       "id": 7,
                       "email": "michael.lawson@reqres.in",
                       "first_name": "Michael",
                       "last_name": "Lawson",
                       "avatar": "https://reqres.in/img/faces/7-image.jpg"
                   },
                   {
                       "id": 8,
                       "email": "lindsay.ferguson@reqres.in",
                       "first_name": "Lindsay",
                       "last_name": "Ferguson",
                       "avatar": "https://reqres.in/img/faces/8-image.jpg"
                   },
                   {
                       "id": 9,
                       "email": "tobias.funke@reqres.in",
                       "first_name": "Tobias",
                       "last_name": "Funke",
                       "avatar": "https://reqres.in/img/faces/9-image.jpg"
                   },
                   {
                       "id": 10,
                       "email": "byron.fields@reqres.in",
                       "first_name": "Byron",
                       "last_name": "Fields",
                       "avatar": "https://reqres.in/img/faces/10-image.jpg"
                   },
                   {
                       "id": 11,
                       "email": "george.edwards@reqres.in",
                       "first_name": "George",
                       "last_name": "Edwards",
                       "avatar": "https://reqres.in/img/faces/11-image.jpg"
                   },
                   {
                       "id": 12,
                       "email": "rachel.howell@reqres.in",
                       "first_name": "Rachel",
                       "last_name": "Howell",
                       "avatar": "https://reqres.in/img/faces/12-image.jpg"
                   }
               ],
               "support": {
                   "url": "https://reqres.in/#support-heading",
                   "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
               }
           }, "!!!Incorrect body response!!!"
    print("\nBody response is correct")


# Test body for special value from response
def test_special_conytent():
    assert jsonpath.jsonpath(response.json(), "total_pages") == [2], "!!!Incorrect special value!!!"
    print("\ntotal_pages = 2")
