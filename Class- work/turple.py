import collections


def unpack_collection(collection):
    result = [0,0,0,0]

    for index in range(4):
        result[index] = collection[index]

    return result

#my_list = [1,2,3,4,5,6,7,8,9]

#print(unpack_collection(my_list))

def unpacking_collection(numbers):

    first_number, second_number, third_number, *others = numbers

    return  first_number, second_number, third_number, others

#print(unpacking_collection(my_list))

def slice_collection(numbers):
    return numbers[0:8:2]
#print(slice_collection(my_list))


def is_odd(numbers):
    return numbers % 2 == 1

def filter_collection(collections):
    return list(filter(is_odd, collections))

#print(filter_collection(my_list))

def filter_with_lambda(collections):
    return list(filter(lambda number: number % 2 == 1, collections))
#print(filter_with_lambda([33,22,8,9,6,2,7]))

def sum_collection(collection):
    sum_all_numbers = sum(map(lambda number:number, collection))
    return sum_all_numbers

print(sum_collection([2,3,4]))
