import requests
url ="https://ginger-turn-ce0.notion.site/User-Agent-1442045d242f8066a254d5de4104455b?pvs=4"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("page.html", "w", encoding="utf8") as f:
  f.write(res.text)
