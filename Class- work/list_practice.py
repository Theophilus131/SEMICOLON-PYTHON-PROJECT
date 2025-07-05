import collections


def modify_collection(collections):
    for i in range(len(collections)):
        collections[i] *= 2
numbers = [1,2,3,4,5,6,7,8,9]

modify_collection(numbers)
print(numbers)

def passing_a_turple_into_a_function(numbers):
    numbers = (10,20,30,40,50,60,70,80,90)

