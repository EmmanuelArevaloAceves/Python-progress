from itertools import count
from operator import truediv


def max (a, b):
    if a > b:
        return a
    else:
        return b


def max_of_tree (a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

def median (a, b, c):
    if (a > b and a < c) or (a < b and a > c):
        return a
    if (b > a and b < c) or (b < a and b > c):
        return b
    else:
        return c

def my_len(palabra):
    counter = 0
    for element in palabra:
        counter += 1
    return counter

def my_sum_mult(lsita):
    total_sum = 0
    total_mult = 1
    for num in lsita:
        total_sum += num
        total_mult *= num
    return total_sum,total_mult

def my_inverso(palabra):
    inverso = ""
    for i in range(len(palabra) - 1, -1, -1):
        inverso += palabra[i]
    return inverso

def my_palindromo(palabra):
    inverso = my_inverso(palabra)
    if palabra == inverso:
        return True
    else:
        return False

def my_compare_list_on_list(list1, list2):
    for word in list1:
        for word2 in list2:
            if word == word2:
                return True
    return False

def my_times_character (n ,char):
    resultado = ""
    for i in range (n):
        resultado += char
    return resultado

def my_procedure(lista):
    for element in lista:
        print(my_times_character(element, "*"))
















#PRACTICA DE SINTAX

def is_even (a):
    if a % 2 == 0:
        return True
    else:
        return False

def is_odd (a):
    if a % 2 == 0:
        return False
    else:
        return True

def is_factor (a, b):
    if b % a == 0:
        return True
    else:
        return False

def is_multiple (a, b):
    if a % b == 0:
        return True
    else:
        return False

def is_vowel (char):
    vocales = ['a', 'e', 'i', 'o', 'u']
    if char.lower() in vocales:
        return True
    else:
        return False

def is_consonant (char):
    vocales = ['a', 'e', 'i', 'o', 'u']
    if char.lower() in vocales:
        return False
    else:
        return True