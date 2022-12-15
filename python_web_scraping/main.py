from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")

ycWebPage = response.text

soup = BeautifulSoup(ycWebPage, "html.parser")
# # print(soup.find(name="a").get("href"))
#
# maks = str
#
# all_scores = soup.find_all(name="span", class_="score")
# enB = int(all_scores[0].string.strip("points"))
#
# for i in all_scores:
#     if int(i.string.strip("points")) > enB:
#         enB = int(i.string.strip("points"))
#         maks = str(i)

# all_links = soup.find_all(name="span", class_="titleline")
# print(all_links[0].getText())
# print(all_links[0].find(name="a").get("href"))


all_links_list = [link.find(name="a").get("href") for link in soup.find_all(name="span", class_="titleline")]
all_scores_list = [int(i.string.strip("points")) for i in soup.find_all(name="span", class_="score")]
all_titles_list = [title.getText() for title in soup.find_all(name="span", class_="titleline")]

maks = max(all_scores_list)
print(f"The maksimum upvote value is {maks} in this page.")
order = all_scores_list.index(maks)
print(f"The title of this article: {all_titles_list[order]}")
print(f"İf you interested ,you can read in this link: {all_links_list[order]}")
