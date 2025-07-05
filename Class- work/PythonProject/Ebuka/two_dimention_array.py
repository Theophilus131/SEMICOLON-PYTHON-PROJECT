
# This code demonstrates how to iterate through a two-dimensional array (list of lists) in Python.
def my_function():
    scores = [[78, 45, 70, 59], [56, 89, 90, 67], [45, 78, 90, 100]]
    for index,score in enumerate(scores):
        for inner_index, inner_value in enumerate(score):

            print(f"inner value:", inner_value)

#collect the number and return it in words
def convert_numbers_to_words(number):
    number_to_words = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten'

    }

    #return number_to_words[numbers]
    return number_to_words.get(numbers, "invalid number")


def iterating_through_dictionary():
    days_per_month = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31
    }

    for month, days in days_per_month.items():
        print(f"{month} has {days} days.")

iterating_through_dictionary()


#if __name__ == '__main__':
    #numbers = int(input("Enter number: "))
    #number_to_words = convert_numbers_to_words(numbers)
    #print(f"The number {numbers} is: {number_to_words} ")







