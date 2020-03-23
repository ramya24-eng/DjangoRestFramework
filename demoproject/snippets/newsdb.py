from snippets.models import News
from snippets.serializers import NewsSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from newsapi import NewsApiClient
import json
import urllib3
import psycopg2
from psycopg2.extensions import AsIs

conn = psycopg2.connect(database="djangorestdb", user="postgres", password="postgres123", host="127.0.0.1", port="5432")
cur = conn.cursor()

newsapi = NewsApiClient(api_key="eb543432c3bb4da8af5653c66ca2e805")
topheadlines = newsapi.get_top_headlines(category='business', language='en', country='in')
articles = topheadlines['articles']
for i in articles:
    #a = json.dumps(articles[i])  # json
    # datajson=json.loads(articles) #string
    # articles = datajson['articles']
    source = i['source']['name']
    print(source)
    author = i['author']
    title = i['title']
    description = i['description']
    url = i['url']
    urltoimage = i['urlToImage']
    timestamp = i['publishedAt']
    content = i['content']

cur.execute("INSERT INTO snippets_news(Source, Author, Title, Description, Url, UrlToImage, PublishedAt, Content)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
            (source, author, title, description, url,urltoimage, timestamp, content));
conn.commit()
cur.close()

