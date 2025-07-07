def max_of_list(lista):
    max_list = lista[0]
    for element in lista:
        if element > max_list:
            max_list = element
    return max_list

def large_word (lista):
    word_large = ""
    number_word_large = 0

    for word in lista:
        counter = 0
        for letter in word:
            counter += 1

        if counter > number_word_large:
            number_word_large = counter
            word_large = word

    return word_large, number_word_large

def filter_words_by_length(words_list, n):
    return [word for word in words_list if len(word) > n]

def count_uppercase_letters(text):
    count = 0
    for char in text:
        if char.isupper():
            count += 1
    return count

def binary_to_integer(binary_string):
    return int(binary_string, 2)

def calculate_ages(current_year, people_info):
    age_results = []
    for name, birth_year in people_info:
        age = current_year - birth_year
        age_results.append((name, age))
    return age_results

def count_ages_above_twenty(ages_tuple):
    return len([age for age in ages_tuple if age > 20])

def count_names_starting_with_letter(names_list, letter):
    return len([name for name in names_list if name.lower().startswith(letter.lower())])

def count_vowels(word):
    vowels = "aeiou"
    result = {vowel: 0 for vowel in vowels}
    for char in word.lower():
        if char in result:
            result[char] += 1
    return result

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)