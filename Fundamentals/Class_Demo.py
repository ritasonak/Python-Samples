import urllib2
import sys


def fetch_words(url):
    story = urllib2.urlopen(url)
    story_words = []
    for line in story:
        line_words = line.split()
        for word in line_words:
            story_words.append(word)
    return story_words


def print_word(story_words):
    for word in story_words:
        print(word)


def main1(url):
    words = fetch_words(url)
    print_word(words)


if __name__ == "__main__":
    # main1(sys.argv[1])
    main1("http://sixty-north.com/c/t.txt")

# Formats of import-
# import Class_Demo
# from Class_Demo import main1
# from Class_Demo import(fetch_words, print_word)
# from Class_Demo import *
