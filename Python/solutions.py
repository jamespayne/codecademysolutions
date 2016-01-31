# Reverses text any text given as input

# def reverse(text):
#     textlength = len(text)
#     output = ''
#     counter = textlength-1
#     for char in range(textlength,0,-1):
#         print counter
#         output += text[counter]
#         counter -= 1
#     return output
# reverse('hello')

# Removes any vowels from a string

# def anti_vowel(text):
#     output = ''
#     for char in text:
#         if char not in 'aeiouAEIOU':
#             output = output + char
#     return output
# anti_vowel("Catepillar")

# Function to find a scrabble word score total

# score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
#          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
#          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
#          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
#          "x": 8, "z": 10}
#
# def scrabble_score(word):
#     word = word.lower()
#     total = 0
#     for char in word:
#         for key in char:
#             total+=score[key]
#     return total
# scrabble_score("xenophobia")

# A function that censors words from text

# def censor(text,word):
#     word = word.lower()
#     words = text.split()
#     for item in words:
#         if item == word:
#             words[words.index(item)] = "*" * len(item)
#     return " ".join(words)
# censor('I like this shit', 'shit')

# Finds the number of times an item occurs in a list

# def count(sequence, item):
#     count = 0
#     for listitem in sequence:
#         if listitem == item:
#             count += 1
#     return count
# count([1,2,"cat",1, "cat"], "cat")

# Removes all the odd numbers from a list

# def purify(content):
#     results = []
#     for item in content:
#         if item % 2 == 0:
#             print "Found item"
#             results.append(item)
#     return results
#
# purify([3,2,4,9,1])

# Finds the product of an array of numbers

# def product(ints):
#     total = 1
#     for item in ints:
#         total *= item
#     return total
# product([3,3,5])

# Removes duplicate values from a list

# def remove_duplicates(values):
#     print values
#     results = []
#     for item in values:
#         if item not in results:
#             results.append(item)
#     return results
# remove_duplicates([1,1,2,2])
