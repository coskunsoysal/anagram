__author__ = 'coskun.soysal'

import sys
from collections import defaultdict

class Anagram(object):

    """
    Check all anagram words in a file
    """

    def __init__(self):
        """
        Initilaze method
        :return:
        """
        self._DEFAULT_FILE = "wordsEn.txt"
        self.result = ""
        self.words_by_count = defaultdict(list)
        file = raw_input("Enter file name: ") or self._DEFAULT_FILE
        self.file = file
        list_of_words = self.file2words(self.file)

        for word in list_of_words:
            self.words_by_count[len(word)].append(word)
        del list_of_words

        count = 0
        for wc in self.words_by_count:
            for word in self.words_by_count[wc]:
                first = False
                del self.words_by_count[wc][0]
                for word2 in self.words_by_count[wc]:
                    if self.is_anagram_of(word, word2):
                        if first == False:
                            count=count+1
                            self.result += "".join([str(count),"   ", word,"   ", word2])
                            first=True
                        else:
                            self.result += "".join(["      ",word2])

        self.write_to_file("result.txt",self.result)

    def file2words(self, file='wordEn.txt'):
        """
        Convert txt file to list of words
        :param file: Input file for given word list
        :return: list of given words
        """
        try:
            with open(file, 'r') as f:
                ret = []
                for line in f:
                    ret += line.split()
                return ret
        except IOError:
            print "%s is not a valid file." % file
            sys.exit()

    def is_anagram_of(self, word1, word2):
        """
        Compare two words for anagram test
        :param word1:
        :param word2:
        :return: True or False if they are anagram
        """
        if len(word1) == len(word2):
            return word1.lower!= word2.lower and word1 == ''.join(sorted(word2))
        else:
            return False

    def write_to_file(self, filename, anagrams):
        """
        Write anagram words to file
        :param filename: Output file
        :param anagrams: Anagram string
        :return:
        """
        f = open(filename, "w")
        f.write(anagrams)
        f.close()

Anagram()