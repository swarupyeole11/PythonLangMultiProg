import requests

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
  }

headers =  {
    'Content-type': 'application/json; charset=UTF-8',
  }

# two ways to call the same post request 
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data, headers=headers)
r = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)
print(response.json())
print(r.json())