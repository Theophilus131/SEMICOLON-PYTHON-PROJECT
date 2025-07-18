

def myFunction(word, ce):

    if len(word) == 0:
        middle = len(word)//2

        return word[:middle] + ce + word[middle:]
    else:
        return word + ce

if __name__ == '__main__':
   print(myFunction("hello","ce"))
   print(myFunction("test","ce"))

