import json
import re
import string

def get_britain(fp):
    text = {i: json.loads(line) for i, line in enumerate(fp)}

    return next((text[i]['text'] for i in range(len(text)) if text[i]['title'] == "イギリス"))


fp = open("jawiki-country.json", encoding='utf-8')

text = get_britain(fp)

fp.close()

for line in re.findall('(<ref>.+</ref>)', text):
    line = re.sub('(<ref>|</ref>|)', '', line)
    for ref in re.findall('http[a-zA-Z{}]+'.format(string.punctuation), line): print(ref)

