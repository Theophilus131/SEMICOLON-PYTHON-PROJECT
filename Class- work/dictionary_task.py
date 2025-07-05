
def my_function(word):
    my_dictionary = {}
    for word in word:
        if word in my_dictionary:
            my_dictionary[word] += 1
        else:
            my_dictionary[word] = 1
    return my_dictionary;


def my_function2(word):

    return {letter : word.count(letter) for letter in word}
        
if __name__ == "__main__":
    #print("occurrence of the word:", my_function("google"))
    print("occurrence of the word:", my_function2("google"))




