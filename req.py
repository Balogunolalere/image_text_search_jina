import requests
import json

reqUrl = "https://orange-wildebeest-apparatus.wayscript.cloud/api/v1/text2image/search"

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Content-Type": "application/json" 
}

payload = json.dumps({
  "host": "grpcs://nowapi-ef7f7d45db.wolf.jina.ai",
  "port": 31080,
  "jwt": {},
  "limit": 10,
  "text": "milo"
})

response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

for i in response.json():
    print(i['scores'])
    print('/n')
    #print(i['blob'])
    #print(i['score'])
    #print('/n')

