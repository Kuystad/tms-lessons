def get_longest_word(txt: str):
    return max(txt.split(), key=len)

print(get_longest_word('Hello world'))