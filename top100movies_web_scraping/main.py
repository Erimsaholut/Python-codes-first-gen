from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

with open("top100movies.txt", "w") as notes:
    for i in all_movies:
        notes.write(f"{i.text}\n")
