import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_nato = list(df.letter)
code_nato = list(df.code)
# nato_dict = {letter: code for (letter, code) in zip(alphabet_nato, code_nato)} - do the same thing that code below
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}


# print(nato_dict)

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError as error:
        print(f"Sorry this {error} is not accepted, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
