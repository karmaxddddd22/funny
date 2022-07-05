import requests 

url = input("URL?:> ")

request_response = requests.head(url)
status_code = request_response.status_code
up = status_code == 200

print(up)

True
