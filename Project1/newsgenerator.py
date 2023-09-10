import requests
import json
query = "What type of news are you intrested in ?"
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-07-23&sortBy=publishedAt&apiKey=API_KEY"
r = requests.get(url)
news = json.loads(r.text)
print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("----------------------------------------------------------")