#
# Author: Amy Collins
# Date: 24-03-2017
#

from bs4 import BeautifulSoup
import urllib

try:
    with open('Python_Questions.txt', 'w') as log_file:

        hyperlink = 'http://www.javatpoint.com/python-interview-questions'
        r = urllib.urlopen(hyperlink).read()
        soup = BeautifulSoup(r,"lxml")
        link = soup.find_all("h3", {"class" : "h3"})
        for j in link:
           log_file.write(j.text + '\n')
        
    log_file.close()
        
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    time.sleep(5)
    pass
except ValueError:
    print "Could not convert data to an integer."
