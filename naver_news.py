import os
import sys
import urllib.request
import urllib.parse
import json

client_id = "YhzRYGzeaKX1tvCozbQA"
client_secret = "*"

encText = urllib.parse.quote("악성메일 -출시")

url = "https://openapi.naver.com/v1/search/news?query=" + encText  # JSON 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()

if rescode == 200:
    response_body = response.read()
    response_json = json.loads(response_body.decode('utf-8'))
    news_articles = response_json['items']

    for article in news_articles:
        title = article['title']
        originallink = article['originallink']
        description = article['description']
        pubDate = article['pubDate']

        print("제목:", title)
        print("원본 링크:", originallink)
        print("설명:", description)
        print("발행일:", pubDate)
        print("-" * 50)
else:
    print("Error Code:" + str(rescode))

#startdate = "2023.07.30"
#enddate = "2023.08.13"
#client_id = "*"
#client_secret = "*"
