#! python3
import requests, os, bs4, re

lastChapterNum = 1084
lastChapter = "https://read-onepiece.one/comic/one-piece-chapter-" + str(lastChapterNum)

url_main = "https://read-onepiece.one/"


print(url_main)

os.makedirs('OnePiece', exist_ok=True)

print("Downloading ")
res_main = requests.get(url_main)
res_main.raise_for_status()
soup_main = bs4.BeautifulSoup(res_main.text, "html.parser")



# print(soup)


#Look for link to new chapter

# print(soup.body.find_all("a", href=re.compile(lastChapter)))

result = soup_main.body.find_all("a", href=re.compile(lastChapter))

print(result)

if lastChapter in str(result):
    print("New chapter found")
    res = requests.get(lastChapter)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.content)

    
else:
    print("No new chapter today")