##
#   source pour ce code:
#   https://www.geeksforgeeks.org/extract-all-the-urls-from-the-webpage-using-python/
#   https://stackoverflow.com/questions/15241338/recursively-search-for-a-file-on-a-website-w-directory-browsing
##

import urllib.request
from bs4 import BeautifulSoup

read_list = []

def RecurseLinks(base):

    f = urllib.request.urlopen(base)
    soup = BeautifulSoup(f.read(), 'lxml')
    for anchor in soup.find_all('a'):
        href = anchor.get('href')
        if (href != '../'):
            if (href.endswith('/')):
                RecurseLinks(base + href) # make recursive call w/ the new base folder
            elif (href == "README"):
                readme = urllib.request.urlopen(base + href).read()
                if readme not in read_list:
                    print ('Found README -> ['+ base + href + ']')
                    read_list.append(readme)
                    print (readme)



# call the initial root web folder change xxx.xxx.xxx.xxx:xxxx by your vm adress and port
RecurseLinks('http://xxx.xxx.xxx.xxx:xxxx/.hidden/')