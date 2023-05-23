#! python3
import requests, os, bs4, re, lxml

newChapterNum = 1084
newChapter = "https://read-onepiece.one/comic/one-piece-chapter-" + str(newChapterNum)

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

result = soup_main.body.find_all("a", href=re.compile(newChapter))

print(result)

if newChapter in str(result):
    print("New chapter found")
    res = requests.get(newChapter)
    res.raise_for_status()
    soup_new = bs4.BeautifulSoup(res.content, 'lxml')
    images = soup_new.select('img')
    print(len(images))

    for image in images:
            print(image['data-src'])



else:
    print("No new chapter today")