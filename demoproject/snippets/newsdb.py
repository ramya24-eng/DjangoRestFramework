from snippets.models import News
from newsapi import NewsApiClient
import psycopg2
from decouple import config

conn = psycopg2.connect(database="djangorestdb", user="postgres", password="postgres123", host="127.0.0.1", port="5432")
cur = conn.cursor()

newsapi = NewsApiClient(api_key=config('api_key'))
categories=['business','technology','health','entertainment']
for cat in categories:
    topheadlines = newsapi.get_top_headlines(category=cat, language='en', country='in')
    articles = topheadlines['articles']
    for i in articles:
       category=cat
       source = i['source']['name']
       author = i['author']
       title = i['title']
       description = i['description']
       url = i['url']
       urltoimage = i['urlToImage']
       #print(category)
       timestamp = i['publishedAt']
       content = i['content']

    News.objects.create(category=category,source=source,author=author,title=title,description=description,url=url,urltoimage=urltoimage,publishedat=timestamp,content=content)

    #cur.execute("INSERT INTO snippets_news(source, author, title, description, url, urlToImage, publishedAt, content)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(source, author, title, description, url, urltoimage, timestamp, content));
conn.commit()
cur.close()

