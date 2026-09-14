import requests #pip install requests

# API klic

def getCurrTemp(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m&timezone=Europe%2FBerlin&forecast_days=1"
    call = requests.get(url).json()

    return call["current"]["temperature_2m"]

#najdi najtoplejše mesto
cities = [
    ("Ljubljana", 46.0511, 14.5051),
    ("Maribor", 46.5558, 15.6459),
    ("Celje", 46.2309, 15.2604),
    ("Kranj", 46.2389, 14.3556),
    ("Koper", 45.5482, 13.7296),
    ("Novo mesto", 45.8040, 15.1689),
    ("Velenje", 46.3572, 15.1128),
    ("Ptuj", 46.4201, 15.8702),
    ("Trbovlje", 46.1541, 15.0518),
    ("Kamnik", 46.2259, 14.6121)
]

getCurrTemp(40.885053663255306, 14.290100010351116)
"""
# klic HTML strežnik
base_url = "https://www.google.com/"
call = requests.get(base_url)

print(call.text)
"""