# To run this, you need to install BeautifulSoup if you aren't using anaconda
# https://pypi.python.org/pypi/beautifulsoup4

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import unittest


def getSumSpans(url):
    
    """ return a sum of all of the text values in the span tags at the passed url
    r
        url -- a uniform resource locator - address for a web page

    """
    
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('span')
    
    total = 0
    
    for tag in tags:
        total = total + int(tag.text)
    return total  


def followLinks(url, numAnchor, numTimes):
    """ Repeat for numTimes. Find the url at numAnchor position (the first link is at position 1) at
        the current url and use that as the new url
        return the text in the a tag from the last url that you process

        url -- a uniform resource locator - address for a web page
        numAnchor -- the position of the anchor (a tag) you are looking at on the page - the first link is position 1
        numTimes -- the number of times to repeat the process of finding the new url
    """

    
 

   #The position of link relative to first link
    count = int(numTimes) -1 #The number of times to be repeated
    urltext = ''
    while count >= 0:
    
        html = urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        tags = soup('a')
        url = tags[int(numAnchor) - 1].get("href", None)
        urltext = tags[int(numAnchor) - 1].text
        count = count -1
        
    print(urltext)
    return urltext

def getGradeHistogram(url):
    """ return a sorted tuple with the grade range (such as 90, 80, etc) and the number of grades in that range
        url -- a uniform resource locator - address for a web page
    """

    pass


class TestHW7(unittest.TestCase):

    def test_sumSpan1(self):
        self.assertEqual(getSumSpans("http://py4e-data.dr-chuck.net/comments_42.html"), 2553)

    def test_sumSpan2(self):
        self.assertEqual(getSumSpans("http://py4e-data.dr-chuck.net/comments_132199.html"), 2714)

    def test_followLinks1(self):
        self.assertEqual(followLinks("http://py4e-data.dr-chuck.net/known_by_Fikret.html",3,4), "Anayah")

    def test_followLinks2(self):
        self.assertEqual(followLinks("http://py4e-data.dr-chuck.net/known_by_Charlie.html",18,7), "Shannah")

    #def test_getGradeHistogram(self):
    #    self.assertEqual(getGradeHistogram("http://py4e-data.dr-chuck.net/comments_42.html"), [(90, 4), (80, 4), (70, 7), (60, 7), (50, 6), (40, 3), (30, 5), (20, 4), (10, 6), (0, 4)])


unittest.main(verbosity=2)
