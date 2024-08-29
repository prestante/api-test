import requests

url = 'https://api.chucknorris.io/jokes/random'
result = requests.get(url)

print(f"Status Code: {result.status_code}")
assert 200 == result.status_code
print(result.text)
