student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
np_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
np_dict = {row.letter: row.code for (index, row) in np_alphabet.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_input = input("Type your message: ")
    try:
        output_list = [np_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()