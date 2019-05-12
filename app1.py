import json
from difflib import get_close_matches

data = json.load(open("data.json")) # type(data) <class 'dict'> json will be changed to dictionary

def get_case_insensitive_key_value(input_dict, key):
    # dictionary key case insensitive search with a one liner:
    return next((value for dict_key, value in input_dict.items() if dict_key.lower() == key.lower()), None)

def translate(word):
    if get_case_insensitive_key_value(data, word):
        return get_case_insensitive_key_value(data, word)
    elif len(get_close_matches(word, data.keys())) > 0:
        closeMatch = get_close_matches(word, data.keys())
        userValidation = input("Did you mean %s instead? Enter Y if yes, or N if no: " % closeMatch[0])
        if userValidation.lower() == "y":
            return data[closeMatch[0]]
        elif userValidation.lower() == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your Query"
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter a Word: ")

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
