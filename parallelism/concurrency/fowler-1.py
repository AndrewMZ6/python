import requests


response = requests.get('https://example.com/')
items = response.headers.items()
headers = [f'{key}:{header}' for key, header in items]
print(headers)
formatted_headers = '\n'.join(headers)

with open("myheaders.txt", 'w') as file:
	file.write(formatted_headers)