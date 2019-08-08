class HelloTest:
    def __init__(self):
        print('Hello class instatiation.')

    def loader(self):
        print('loader function')
        words = ['chandu', 'kumar', 'soni', 'chandan']
        for word in words[:]:
            if len(word) > 6:
                words.insert(0, word)
        print('Index\tContent')
        for index in range(len(words)):
            print(index, '\t', words[index])


if __name__ == '__main__':
    HelloTest().loader()
