#Exercise 1

from decimal import Decimal

my_list = ['Getafe', 'Sevilla', 'Valencia', 'Girona']
print(my_list)

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

my_float = 12.3
print(my_float)

my_integer = 18
print(my_integer)

my_decimal = Decimal('10.5')
print(my_decimal)

my_dictionary = {
    'club': 'Real Sociedad',
    'liga': 'La Liga' ,
    'puesto': 6
}
print(my_dictionary)

#Exercise 2

import math

print(math.ceil(my_float))

#Exercise 3

print(math.sqrt(my_float))

#Exercise 4

first_key_value = list(my_dictionary.items())[0]
print(first_key_value) 

#Exercise 5

print(my_tuple[1])

first, second, third, fourth, fifth = my_tuple
print(second)

#Exercise 6

my_list.append('Barcelona')
print(my_list)

#Exercise 7

my_list[0] = 'Eibar'
print(my_list)

#Exercise 8
my_list.sort()
print(my_list)

#Exercise 9
my_tuple += ('Exercise',)
print(my_tuple)