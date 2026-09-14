# https://hackmd.io/@lukac/api1
import requests
# Izpiši trenutno temperaturo za poljuben kraj

def trenutna_temp(lat, lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m&timezone=auto&forecast_days=1"
    call = requests.get(base_url).json()
    print(call["current"]["temperature_2m"])

trenutna_temp(45.12, 14.5)