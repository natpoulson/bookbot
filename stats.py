def get_num_words(input):
    return len(input.split())

def get_num_chars(input):
    chars = {}
    for char in input:
        if char.lower() not in chars:
            chars[char.lower()] = 1
        else:
            chars[char.lower()] += 1
    return chars

def sort_num(dict):
    return dict["num"]

def create_sorted_dictionary(input):
    new_dict = []
    for i in input.keys():
        new_dict.append({"char": i, "num": input[i]})
    new_dict.sort(reverse=True,key=sort_num)
    return new_dict
