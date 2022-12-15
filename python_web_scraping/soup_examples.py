from bs4 import BeautifulSoup

# import lxml

with open("website.html") as fp:
    contents = fp.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify())
# print(soup.h3) ,p
# print(soup.h1.string)
# print(soup.prettify())
# print(soup.a) # it gives you the first anchor tag

all_anchor_tags = soup.findAll(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

heading = soup.find(name="h1", id="name")
# print(heading)

secilmis_heading = soup.find(name="h3", class_="heading")
secilmis_headings = soup.findAll(name="h3", class_="heading")
# print(secilmis_heading)

linklink = soup.select(selector="p a")
# print(linklink)

name = soup.select_one(selector="#heading")
# print(name)

head = soup.select(".heading")
# print(head)
