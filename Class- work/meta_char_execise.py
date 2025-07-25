import re

phoneNumber =  "123-456-7890yyyyy"

pattern = re.compile((r'(\d{3}-\d{3}-\d{4})'))

matches = pattern.findall(phoneNumber)
print(matches)




