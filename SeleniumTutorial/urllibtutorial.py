import requests

payload = {'page':2,'count':25}

r = requests.get('https://httpbin.org/get',params = payload)

print(r.text)



#with open('comic.png','wb') as f:
#	f.write(r.content)



