#!/usr/bin/python
#
# createtimedir.py
# created by Raymond Jongeneel
# creation date june 21, 2014
#
import datetime
import os
def createtimedir():
    d = datetime.datetime.now()
    datedir = '{:%Y-%m-%dH%H.%M.%S}'.format(d)
    if not os.path.exists(datedir):
        os.mkdir(datedir)

if __name__ == "__main__":
    createtimedir()
