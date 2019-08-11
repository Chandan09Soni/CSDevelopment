
import sys
# from pyspark.sql import SparkSession
# import boto3
from pyspark.sql import SparkSession


class HelloTest:
    """This is a test class"""
    def __init__(self):
        """This is the intialization"""
        print('This is initializatoin function')
        self.app_name = self.__class__.__name__
        self.spark_session = SparkSession.builder.appName(self.app_name).\
            getOrCreate()

    def loader(self):
        """This is a main entry point of class"""
        print(self.app_name)
        print(' loader function ')
        print('Python version is {}'.format(sys.version))
        words = ['chandu', 'kumar', 'soni', 'chandan']
        for word in words[:]:
            if len(word) > 6:
                words.insert(0, word)
        print('Index \t Content')
        for index, word in enumerate(words):
            print(str(index) + '\t' + word)


if __name__ == '__main__':
    HelloTest().loader()
