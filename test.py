import requests

r = requests.get('http://localhost:5001/sitf?k=0.82', verify=False)
print(r.json())