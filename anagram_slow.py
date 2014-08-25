__author__ = 'coskun.soysal'

import sys


class Anagram(object):

    """
    Check all anagram words in a file
    """

    def __init__(self):
        self._DEFAULT_FILE = "wordsEn.txt"
        self.result = ""
        self.lengths = []
        file = raw_input("Enter file name: ") or self._DEFAULT_FILE
        self.file = file
        list_of_words = self.file2words(self.file)

        try:
            for word in list_of_words:
                del list_of_words[0]
                for word2 in list_of_words:
                    if self.is_anagram_of(word, word2):
                        self.result += "word word2\n"
                        print word, word2

            self.write_to_file("result.txt", self.result)
        except:
            print "Unexpected Error"

    def file2words(self, file='wordEn.txt'):
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

        if len(word1) == len(word2):
            return word1.lower!= word2.lower and word1 == ''.join(sorted(word2))
        else:
            return False

    def write_to_file(filename, anagrams):
        f = open(filename, "w")
        f.write("Anagrams found: " + str(len(anagrams)) + "\n")
        for anagram in anagrams:
            for word in anagram:
                f.write(word + " ")
            f.write("\n")
        f.close()


Anagram()