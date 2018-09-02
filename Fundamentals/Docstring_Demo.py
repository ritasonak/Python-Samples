"""Retrieve and print words from a URL

"""
import urllib2


def fetch_words(url):
    """Fetch a list of words from URL.

    :param
        url: The URL of a UTF-8 text document.
    :return:
        A list of strings containing the words from the document.
    """
    story = urllib2.urlopen(url)
    story_words = []
    for line in story:
        line_words = line.split()
        for word in line_words:
            story_words.append(word)
    return story_words