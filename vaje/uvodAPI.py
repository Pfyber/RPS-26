# slovarji (dictionary)

slovar = {"ključ" : "vrednost",
          "ključ2" : "vrednost2"} 
print(slovar)
#dostop
print(slovar["ključ2"])

# raznoliki slovar
razno = {"stevilo" : 6,
         "ime" : "Luka",
         "seznam" : [1,2,3,4],
         "slovar" : {"firma" : "Dacia", "moč": "120kw"}}

print(razno["stevilo"] + 10)
print(max(razno["seznam"]))
print(razno["slovar"]) #{"firma" : "Dacia", "moč": "120kw"}
print(razno["slovar"]["firma"])
print(razno["slovar"]["moč"])



# Open Meteo API
import requests
base_url = "https://api.open-meteo.com/v1/forecast?latitude=46.0511&longitude=14.5051&daily=rain_sum&timezone=Europe%2FBerlin"

call = requests.get(base_url).json()

print(call["daily"]["rain_sum"][0])