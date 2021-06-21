import requests

if __name__ == '__main__':
    print('Hello world!')
    
    response = requests.get('https://swapi.dev/api/people/1')
    print(response.json())

