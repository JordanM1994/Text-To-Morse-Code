import pandas

# Placing the csv data into a dataframe

alphabet = pandas.read_csv("morse_code_files/morse_code.csv")
alphabet_dataframe = pandas.DataFrame(alphabet)

# transforming the csv data into a dictionary

morse_code_alphabet = {row.letter: row.morse_code for (index, row) in alphabet_dataframe.iterrows()}

# Brain - asking for the users words, splitting them into letters and finding the corresponding morse code

is_on = True

while is_on:
    word = input("What would you like to covert to morse code?: ").upper()

    try:
        word_to_code = [morse_code_alphabet[letter] for letter in word]
    except KeyError:
        print('Please only use letters, numbers and any of the following symbols: & @ ) ( : , = ! . - × +  ? / '
              'in the alphabet')
    else:
        is_on = False

# takes the morse code out of a list and into a string below:
code = ""

for word in word_to_code:
    code += f"{word} "

print(code)
