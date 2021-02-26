import requests

def get_currencies(country):
    names = []
    for c in country['currencies']:
        if c['name'] is not None:
            names.append(c['name'])

    return names


code = input("Enter currency code :")
resp = requests.get(f"https://restcountries.eu/rest/v2/currency/{code}")
countries = resp.json()

for c in countries:
    currencies = ",".join(get_currencies(c))
    print(f"{c['name']:50} {c['region']:20} {currencies}")


