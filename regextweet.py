import re


with open('tweets', 'r') as f: 
	read_data = f.readlines()
	for l in read_data:
		l = re.sub(r'#\w+ ?', '', l)
		l = re.sub(r'http\S+', '', l)
		l = re.sub(r'@\w+ ?', '',l)
		l = re.sub(r'\"? *RT *:*','',l)
		l = re.sub(r'\"','',l)
		print l