import requests   #request-библеотека для работы с API


r = requests.get('https://jsonplaceholder.typicode.com/posts')  #ссылка с адрессом проверки

def test_one():
    assert r.status_code == 200
    print("\n", r.status_code)

