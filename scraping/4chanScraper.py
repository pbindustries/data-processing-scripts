#! python3

import urllib, bs4, requests

#PREPROCESSING
print("Enter thread url")
url = raw_input()
#url = 'http://boards.4chan.org/%s/thread/%s' % boardName,threadNumber
req = requests.get(url)
req.raise_for_status()
soup = bs4.BeautifulSoup(req.text, "lxml")
filevar = soup.find_all("a", class_="fileThumb")

#DOWNLOADING ALL KIND OF FILES
for i in range(len(filevar)):
	webm = 'http:' + filevar[i].get('href')
	urllib.request.urlretrieve(webm, str(i))
	print(str(i) + ' done')