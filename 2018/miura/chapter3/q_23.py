import re
from q_20 import extract

for line in extract('イギリス').split('\n'):
	if re.match('^==', line):
		print(line.strip('='), line.count('=')//2)

