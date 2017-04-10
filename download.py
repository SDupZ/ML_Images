import urllib, urlparse
import os

with open('./myfile.txt') as f:
    for line in f:
        string_split = line.split('~')
        if (len(string_split) == 2):
            name = string_split[0]
            url = string_split[1]
            url = url.strip('\n')
            split = urlparse.urlsplit(url)
            filename = name +"/" + split.path.split("/")[-1]
            if not os.path.exists(name + '/'):
                os.makedirs(name + '/')
            urllib.urlretrieve(url, filename)

