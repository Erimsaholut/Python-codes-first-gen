import requests

url = "https://rawg-video-games-database.p.rapidapi.com/games"

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)