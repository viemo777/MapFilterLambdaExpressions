def sum_of_two_nums(x):
    return x + x


number_list = [1, 2, 3, 4, 5, 6, 7]

res = map(sum_of_two_nums, number_list)
print(list(res))
print(res)

def is_a_in_string(string):
    if 'a' in string:
        print('String has "a"')
        return True
    else:
        print('String has not "a"')
        return False

string_list = ['hi', 'my', 'may']
print(list(map(is_a_in_string, string_list)))

def is_number_odd(number):
    return number % 2 == 1


number_list = [1, 2, 3, 4, 5, 6, 7]
res = filter(is_number_odd, number_list)
print(res)
print(list(res))

def cube(number):
    return number ** 3


number_list = [1, 2, 3, 4, 5, 6, 7]
print(list(map(cube, number_list)))

# or

print(list(map(lambda number: number ** 3, number_list)))


string_list = ['hi', 'my', 'may']
print(list(map(lambda string: string[-2], string_list)))
