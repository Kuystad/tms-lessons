import re


def generate_words(txt):
    word = re.findall('\w+', txt)
    start = 0
    while start < len(word):
        yield word[start]
        start += 1


if __name__ == '__main__':
    for w in generate_words('mom.washed!frame?'):
        print(w)

    assert ['zxc', 'qwe', 'tyu'] == [w for w in generate_words('zxc. qwe! tyu?')]
    assert ['qqq', 'www', 'eee'] == [w for w in generate_words('qqq!>< www$$ eee&&&')]


