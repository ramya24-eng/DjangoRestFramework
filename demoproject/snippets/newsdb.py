import json
import urllib3
import psycopg2

conn = psycopg2.connect(database="djangorestdb", user="postgres", password="postgres123", host="127.0.0.1", port="5432")
cur = conn.cursor()

http = urllib3.PoolManager()
url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=eb543432c3bb4da8af5653c66ca2e805"

try:
    response = http.request('GET', url)
    data = json.loads(response.data.decode('utf-8'))
    index = 0 #I'm using index as an id_key

    for i in data:
        source = None
        author = None
        title = None
        description =None
        url = None
        urlToImage = None
        publishedAt = None
        content = None

        #var1 = i['var1']
        #var2 = i['var2']
        source = i['source']
        author = i['author']
        title = i['title']
        description = i['description']
        url = i['url']
        urlToImage = ['urlToImage']
        publishedAt = ['publishedAt']
        content = ['content']
        cur.execute("
            INSERT INTO TABLE news
            VALUES (%s, %s, %s, %s, %s, %s ,%s ,%s, %s)",
            (index, source,author,title,description,url,urlToImage,publishedAt,content));
        conn.commit()
        index += 1
    cur.close()
except IOError as io:
    print("ERROR!")