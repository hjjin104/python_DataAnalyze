import requests as req

url = 'https://media.naver.com/press/052/ranking?type=popular'
r = req.get(url)

print(r.status_code)