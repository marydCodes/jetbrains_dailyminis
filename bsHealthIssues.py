# '''Read a link from the input. Get all text paragraphs from all the a tags and single out the topics (not any word or phrase!) starting with the letter S. Print the final list. Beware of empty lines.'''

import requests

from bs4 import BeautifulSoup


url = input()
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
a_tags = soup.find_all('a')
lst = []
topics = ["health-topics", "entity", "topics"]
for tag in a_tags:
    if tag.text.startswith("S") and len(tag.text) > 1:
        for topic in tag.get('href').split("/"):
            if topic in topics:
                lst.append(tag.text)

print(lst)
