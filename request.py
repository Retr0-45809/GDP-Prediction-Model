import requests

url = 'http://127.0.0.1:5000/'
r = requests.post(url,json={'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0})

print(r.json())
