#! python3
import requests, os, bs4, re

lastChapter = str(1082)

url = "https://read-onepiece.one/comic/one-piece-chapter-1082"

os.makedirs('OnePiece', exist_ok=True)

print("Downloading ")
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

#Look for "last chapter" tag

chapterSoup = soup.find_all('a')
text = 'last-chapter'
print(chapterSoup)

for i in chapterSoup:
    if(i.string == text):
        print(i)

#while chapter == []:
#    chapter = soup.select('new-chapter')
#    print("Not latest chapter")
#    lastChapter = str(int(lastChapter)+1)
#    return lastChapter
#else:
    



# for tag in soup.find_all(re.compile("data-src")
