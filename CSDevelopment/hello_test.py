#!/usr/bin/python3
import sys
import boto3
class HelloTest:
    """asdkfjl"""
    def __init__(self):
        """This is the intialization"""
        print('This is initializatoin function')

    def loader(self):
        """This is a main entry point of class"""
        print(' loader function ')
        print(sys.version)
        words = ['chandu', 'kumar', 'soni', 'chandan']
        for word in words[:]:
            if len(word) > 6:
                words.insert(0, word)
        print('Index \t Content')
        for index, word in enumerate(words):
            print(str(index) +'\t'+ word)

if __name__ == '__main__':
    HelloTest().loader()
