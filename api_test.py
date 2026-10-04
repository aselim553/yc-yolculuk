import os
import requests

# API anahtarı koda yazılmaz; ortam değişkeninden okunur.
# Windows: setx OPENWEATHER_API_KEY "anahtarın"  (sonra terminali yeniden aç)
api_key = os.environ.get("OPENWEATHER_API_KEY")
if not api_key:
    raise SystemExit("OPENWEATHER_API_KEY ortam değişkeni tanımlı değil.")

sehir = input("Şehir adı girin: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric&lang=tr"

try:
    yanit = requests.get(url)
    veri = yanit.json()

    sicaklik = veri["main"]["temp"]
    durum = veri["weather"][0]["description"]
    nem = veri["main"]["humidity"]

    print(f"\n{sehir} hava durumu:")
    print(f"Sıcaklık: {sicaklik}°C")
    print(f"Durum: {durum}")
    print(f"Nem: {nem}%")

except Exception as e:
    print("Veri çekilemedi, şehir adını kontrol et!")
