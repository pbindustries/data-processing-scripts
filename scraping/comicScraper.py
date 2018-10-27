# Comic Downloader

#! python3

import urllib, bs4, requests
url = 'http://explosm.net/comics/39/'
base_url = 'http://explosm.net'

for i in range(1,4000):

    req = requests.get(url)
    req.raise_for_status()
    soup = bs4.BeautifulSoup(req.text, "lxml")
    comic = soup.select('#main-comic')
    comicUrl = 'http:' + comic[0].get('src')
    urllib.request.urlretrieve(comicUrl, str(i))
    print(str(i) + ' done')
    next_comic = soup.select('.next-comic')
    url = base_url + next_comic[0].get('href')