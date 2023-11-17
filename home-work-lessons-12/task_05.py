import re


class WordIterable:

    def __init__(self, txt):
        self.txt = re.findall(r'\b\w+\b', txt)
        self.word = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.word < len(self.txt):
            result = self.txt[self.word]
            self.word += 1
            return result
        else:
            raise StopIteration


if __name__ == '__main__':
    for w in WordIterable('mom washed frame'):
        print(w)

    assert ['in', 'the', 'end'] == [w for w in WordIterable('in the end')]
    assert ['every', 'breath', 'u', 'take'] == [w for w in WordIterable('every breath u take')]

