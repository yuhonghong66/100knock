import json
import gzip

def extract(title):
	with gzip.open('jawiki-country.json.gz', mode='r') as f:
		for line in f:
			article = json.loads(line)
			if article['title'] == title:
				return article['text']

if __name__ == '__main__':
	print(extract('イギリス'))

