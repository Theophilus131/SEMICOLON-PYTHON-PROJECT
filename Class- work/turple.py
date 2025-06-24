
def unpack_collection(collection):
    result = [0,0,0,0]

    for index in range(4):
        result[index] = collection[index]

    return result

my_list = [1,2,3,4,5,6,7,8,9]

#print(unpack_collection(my_list))

def unpacking_collection(numbers):

    first_number, second_number, third_number, *others = numbers

    return  first_number, second_number, third_number, others

#print(unpacking_collection(my_list))

def slice_collection(numbers):
    return numbers[0:8:2]
print(slice_collection(my_list))



