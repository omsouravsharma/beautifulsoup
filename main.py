from bs4 import BeautifulSoup
import requests

data = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

yc_webpage = data.text
soup = BeautifulSoup(yc_webpage, 'html.parser')
print(soup.title)
print(soup.prettify())
print(soup.find(name="h3", class_="jsx-4245974604"))
print(soup.select_one(selector="h3"))
all_movies = soup.find_all(name="h3", class_="title")

movie_title = [movie.getText() for movie in all()]
movies = movie_title[::-1]

with open("movies.txt", mode='w') as file:
    file.write(f"{movies}\n")

