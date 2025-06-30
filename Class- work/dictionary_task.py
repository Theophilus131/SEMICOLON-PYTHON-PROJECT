
def my_function(word):
    my_dictionary = {}
    for word in word:
        if word in my_dictionary:
            my_dictionary[word] += 1
        else:
            my_dictionary[word] = 1
    return my_dictionary;

if __name__ == "__main__":
    print("Length of the word:", my_function("google"))





