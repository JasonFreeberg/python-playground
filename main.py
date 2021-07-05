import requests


def triple(num):
    return num * 3


def test_triple():
    assert triple(4) == 12
    assert triple(0) == 0


if __name__ == '__main__':
    print('Hello world!')

    response = requests.get('https://swapi.dev/api/people/1')
    print(response.json())
