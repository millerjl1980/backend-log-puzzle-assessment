#!/usr/bin/env python2
"""
Logpuzzle exercise

Copyright 2010 Google Inc.
Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0

Google's Python Class
http://code.google.com/edu/languages/google-python-class/

Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700]
"GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6)
Gecko/20070725 Firefox/2.0.0.6"

"""
___author___ = "Justin Miller"

# import os
import re
import sys
import urllib.request
import argparse


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # +++your code here+++
    with open(filename, 'r') as rf:
        text = rf.read()
    matches = re.findall(r'GET (\S*puzzle\S*) HTTP', text)
    matches = set(matches) #https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
    matches = sorted(matches)
    full_paths = []
    for match in matches:
        full_paths.append('http://code.google.com' + match)
    return full_paths


def download_images(img_urls):
# , dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # +++your code here+++
    #https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/
    # if not os.path.isdir(dest_dir):
    #     os.mkdir(dest_dir)
    # Image Names
    dest_dir = 'images'
    img_paths = []
    for url , count in enumerate(img_urls):
        img_paths.append(dest_dir + '/img_' + str(url) + '.jpg')
    for paths in img_paths:
        print(paths)

    # Download Images to Directory
    for img, path in zip(img_urls, img_paths):
        urllib.request.urlretrieve(img, path)

    return img_paths


def create_parser():
    """Create an argument parser object"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--todir',
                        help='destination directory for downloaded images')
    parser.add_argument('logfile',
                        help='apache logfile to extract urls from')

    return parser


def main(args):
    """Parse args, scan for urls, get images from urls"""
    parser = create_parser()

    if not args:
        parser.print_usage()
        sys.exit(1)

    parsed_args = parser.parse_args(args)

    img_urls = read_urls(parsed_args.logfile)
    imges = download_images(img_urls)

    # if parsed_args.todir:
    #     download_images(img_urls, parsed_args.todir)
    # else:
    #     print('\n'.join(img_urls))


if __name__ == '__main__':
    main(sys.argv[1:])
