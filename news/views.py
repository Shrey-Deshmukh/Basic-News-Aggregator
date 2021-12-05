from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re
import urllib


# GEtting news from Times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[2:-13] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)





h_r = requests.get("  https://www.thehindu.com/")
h_soup = BeautifulSoup(h_r.content, 'html5lib')

h_headings = h_soup.find_all('div', {'class':'story-card'})

news_title = []
news_images = []
news_url = []
h_news = dict()

for article in h_headings:
    main = article.find_all('a')[0]
    main = str(main)
    link = re.findall(r'href=\"(.*?)\"', main)
    imagelink = article.find_all('img')[0]
    imagelink = str(imagelink)
    image = re.findall(r'data-src-template=\"(.*?)\"', main)

    title = article.find_all('h2')

    title = str(title)

    title1 = title.split("\n")

    if len(title1) != 1:
        news_title.append(title1[2])
        link = str(link)
        h_news[title1[2]] = requests.get(link[2:-3])
    news_images.append(image)
    news_url.append(link)



def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news, 'ht_news': h_news})
