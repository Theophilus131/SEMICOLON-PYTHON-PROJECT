import re

userEmail = "abc@gmail.com"
wrongEmail = "yemi@yemi@gmail,com"

pattern = re.compile(r'[a-zA-Z]+@+gmail\.com')

#matches = pattern.findall(wrongEmail)
#print(matches)

text = "Alice and Bob are Good Friends."
pattern_ = re.compile(r'[A-Za-z]+')
matches = pattern_.findall(text)
print(matches)



sentence = "Hello! How are you doing?"
pattern = re.compile(r'\w+')
matches = pattern.findall(sentence)
print(sentence)


