import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()

large_countries = sorted(countries, reverse=True,
               key=lambda c: c['area'] if c['area'] is not None else 0)
for c in large_countries[:10]:
    print(f"{c['name']:50} {c['area']:10}")


