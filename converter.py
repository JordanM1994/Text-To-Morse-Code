import pandas

alphabet = pandas.read_csv("morse_code_files/morse_code.csv")
alphabet_dataframe = pandas.DataFrame(alphabet)

morse_code_alphabet = {row.letter: row.morse_code for (index, row) in alphabet_dataframe.iterrows()}

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

code = ""

for word in word_to_code:
    code += f"{word} "

print(code)
