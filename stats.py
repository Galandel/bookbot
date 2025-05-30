def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    char_count_dict = dict()
    text = text.lower()
    for char in text:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def sort_on(d):
    return d["num"]

def sort_char_counts(char_count):
    sorted_list = []
    for char in char_count:
        if char.isalpha():
            sorted_list.append({"char": char, "num":char_count[char]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list