def count_words(text):
    words = text.split()
    return len(words)
# Count the words


def count_character(text):
    character_count = {}
    for char in text:
        char = char.lower()
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count
# Count the characters (dictionary)


def sorted_dict(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})

    def sort_on(dict_item):
        return dict_item["count"]
        
    char_list.sort(reverse=True, key=sort_on)
    return char_list


