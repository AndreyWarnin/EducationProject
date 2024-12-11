def all_variants(text):
    start = 0
    end = 1
    while end - start <= len(text):
        s = text[start:end:]
        start += 1
        end += 1
        if end > len(text):
            end = end - start + 1
            start = 0
        yield s

for s in all_variants('abc'):
    print(s)
