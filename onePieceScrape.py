#! python3
import requests, os, bs4, re

lastChapter = str(1082)

url = "https://read-onepiece.one/"

print(url)

os.makedirs('OnePiece', exist_ok=True)

print("Downloading ")
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

print(soup)


#Look for "last-chapter" tag

# Search for a fragment of a string using a regular expression

# text = 'last-chapter'
# pattern = re.compile(html)
# tag_with_fragment = soup.find_all(string=pattern)
# print(tag_with_fragment)        

#while chapter == []:
#    chapter = soup.select('new-chapter')
#    print("Not latest chapter")
#    lastChapter = str(int(lastChapter)+1)
#    return lastChapter
#else:
    



# for tag in soup.find_all(re.compile("data-src")
