def generate_words(txt):
    word = txt.split()
    start = 0
    while start < len(word):
        yield word[start]
        start += 1


if __name__ == '__main__':
    for w in generate_words('mom washed frame'):
        print(w)

    assert ['qqq', 'www', 'eee'] == [w for w in generate_words('qqq www eee')]
    assert ['sss', 'ddd', 'ttt'] == [w for w in generate_words('sss ddd ttt')]
    assert ['aaa', 'fff', 'ggg'] == [w for w in generate_words('aaa fff ggg')]
    assert not ['qqq', 'www', 'eee'] == [w for w in generate_words('qqq.www!eee')]