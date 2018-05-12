from bs4 import BeautifulSoup
import requests

#Method to scrape reviews
def scrapeMal():
    url = "https://myanimelist.net/anime/1/Cowboy_Bebop/reviews?p="
    counter = 0

    for i in range(1,10):
        r  = requests.get(url+str(i))
        print(url)
        data = r.content
        soup = BeautifulSoup(data, "lxml")
        tags = soup.find_all('div',{'class' : 'spaceit textReadability word-break pt8 mt8'})


        for ele in tags:
            file = open("Reviews/cowboy%s.txt" % counter, "w")
            s = ele.get_text()[100:]
            s = s.encode('ascii', errors = 'ignore').decode()
            file.write(s)
            file.close()
            counter+=1

#the XML data seems to have bad structure, it is difficult to parse and extract reviews without some serious RE guru
#attempt to scrape via their API

def apiMalRequest():
    url2 = "https://myanimelist.net /api/anime|manga/search.xml?q=full+metal"
    r  = requests.get(url2)
    data2 = r.json
    print(data2)

#API calls seem buggy at best
#will use scraping for now

scrapeMal()
