import requests

# VVVVIMP : Python executes every request synchornoulsy 

# Get Request 

resp = requests.get("https://jsonplaceholder.typicode.com/posts")
print(resp.json())

# Post Request
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