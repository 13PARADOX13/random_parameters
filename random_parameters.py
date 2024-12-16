def single_root_words(root_word, *other_words):
    same_words = []
    other_words_list = [*other_words]
    for i in other_words_list:
        if root_word.lower() in i.lower():
            same_words.append(i)
        elif i.lower() in root_word.lower():
            same_words.append(i)
    return same_words

print(single_root_words('air', 'AiRplane', 'Airborne', 'ActioN', 'agrEE', 'AIRCRAFT'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
