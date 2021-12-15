import requests

print("Input the URL:")
input_url = str(input())

r = requests.get(input_url)
url_json = r.json()

try:
    print(url_json['content'])
except:
    print("Invalid quote resource!")