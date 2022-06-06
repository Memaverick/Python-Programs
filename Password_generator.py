import random

max_lenght = 8
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

cap_letters =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

combinaly = numbers + small_letters + cap_letters + symbols

random_numbers = random.choice(numbers)
random_small = random.choice(small_letters)
random_cap = random.choice(cap_letters)
random_symbols = random.choice(symbols)

gene_pass = random_numbers + random_small + random_cap + random_symbols

for x in range(max_lenght   ):
    gene_pass = gene_pass + random.choice(combinaly)

print(gene_pass)