

import pandas
data= pandas.read_csv("nato_phonetic_alphabet.csv")
{"A": "Alfa", "B": "Bravo"}
new_dict= {row.letter: row.code for (index, row) in data.iterrows()}
print(new_dict)

def NATOWORD():
    word = input("Enter a word: ").upper()

    try:
        output_list= [new_dict[letter] for letter in word]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        NATOWORD()
    else:

        print(output_list)
NATOWORD()