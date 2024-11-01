
def single_root_words(root_word, *other_words):
    same_words = []
    lower_root_word = root_word.lower()

    for other_word in other_words:
        lower_other_word = other_word.lower()
        if lower_other_word.__contains__(lower_root_word):
            same_words.append(lower_other_word)
        elif lower_root_word.__contains__(lower_other_word):
            same_words.append(lower_other_word)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)