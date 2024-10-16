def single_root_words(root_word, *other_words):
    for word in other_words:
        if word.lower == root_word.lower:
            return other_words
    return None

root_word = 'sky'
other_words = ['wood', 'staff', 'sky', 'angle']
same_words = single_root_words(root_word, *other_words)
print(same_words)