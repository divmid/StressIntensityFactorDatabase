import requests
r = requests.get('http://localhost:5000/sitf?crack_type=3&a1=11&a2=1&d=18', verify=False)
print(r.json())