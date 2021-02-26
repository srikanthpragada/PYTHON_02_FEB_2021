import requests


user = "srikanthpragada123"
resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code != 200:
    print(f"Sorry! Could not get details of user {user}")
    exit()

details = resp.json()
for key,value in details.items():
    print(f"{key:20} {value}")

