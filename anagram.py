__author__ = 'coskun.soysal'

import sys

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
        self.anagrams = {}

    def main(self):
        """
        Main method which runs script
        :return:
        """
        file = raw_input("Enter file name: ") or self._DEFAULT_FILE
        self.file = file
        list_of_words = self.file2words(self.file)

        for word in list_of_words:
            self.anagrams.setdefault(self.order_chars(word), []).append(word)

        count = 0
        for words in self.anagrams.values():
            if len(words) > 1:
                count += 1
                self.result += '%s. %s %s\n' % (str(count).rjust(5, '0'), words[0].ljust(17, ' '), words[1])
                for word in words[2:]:
                    self.result += '%s\n' %  word.rjust(25+len(word), ' ')

        self.write_to_file("result.txt",self.result)

    def order_chars(self, word):
        """
        Order a stings letter alphabetically
        :param word: raw word
        :return: Ordered string
        """
        return ''.join(sorted(word))


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