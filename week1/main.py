from part_1 import *
from part_2 import *

print("PART 1\n")
print("Max:")
print(max(85,86))

print("\nMax of tree:")
print(max_of_tree(89,95,116))

print("\nMedian of tree:")
print(median(10, 5, 7))

print("\nElement sum list:")
print(my_len("Hola"))

print("\nIs vowel true or false:")
print(is_vowel('x'))

print("\nSum or Multiplication of a list:")
print(my_sum_mult([4,5,6]))

print("\nInverse of a list:")
print(my_inverso("Hola"))

print("\nIs palindromo:")
print(my_palindromo("radar"))

print("\nCompare too list:")
print(my_compare_list_on_list([4,5,6], [8,5,9]))

print("\nTimes character:")
print(my_times_character(5,"!"))

print("\nProcedure:")
print(my_procedure([4,5,6]))

print("\nPART 2\n")

print("Max List\n")
print(max_of_list([85,69,67,89,354,234,6842,567842,8742,56742,8841]))

print("\nLarge word")
print(large_word(["Hola", "popo", "compartir"]))

print("\nFilter Words")
print(filter_words_by_length(["apple", "banana", "kiwi", "pineapple"], 5))

print("\nCount uppercase")
print(count_uppercase_letters("Hello WORLD!"))

print("\nBinary to integer")
print(binary_to_integer("1011"))

print("\nCalculate ages")
people = [("Alice", 2000), ("Bob", 1995), ("Charlie", 1988)]
print(calculate_ages(2025, people))

print("\nCalculate ages above twenty")
ages = (18, 25, 30, 15, 22, 10, 35, 40, 19, 23)
print(count_ages_above_twenty(ages))

print("\ncount names starting with '_'")
names = ["Ana", "Luis", "andrea", "Pedro", "Antonio"]
print(count_names_starting_with_letter(names, "a"))

print("\ncount vowels")
print(count_vowels("Educación"))

print("\nleap year")
print(is_leap_year(2024))
print(is_leap_year(1900))


print("\n\n\n\n")

print("PRACTICA DE SINTAX")

#PRACTICA DE SINTAX

print("Is even true or false")
print(is_even(7))

print("Is odd true or false")
print(is_odd(7))

print("Is factor true or false")
print(is_factor(3, 9))

print("Is Multiple true or false")
print(is_multiple(10, 5))

print("Is consonant true or false")
print(is_consonant('f'))