#!/usr/bin/python
#
# createtimedir.py
# created by Raymond Jongeneel
# creation date june 21, 2014
# Purpose: create a directory in the current working directory
# with the name in the format: yyyy-mm-dd h24.mi.ss
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
