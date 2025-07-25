import re

text = "The silent12 Boy, is sick23 today, call this number**0903 king73778"

#pattern =re.findall(r'\b\d+\b', text)

pattern = re.compile(r'1')

matches = pattern.findall(text)

print(matches)