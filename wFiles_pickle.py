import os, pickle
from sys import argv

ad_file = r'D:\python\mypy\addr_book.db'
serialize = __import__('pickle')

def updateDB(i1):
    dict = i1
    ad_f_w = open(ad_file, 'w')
    serialize.dump(dict, ad_f_w)
    ad_f_w.close()

def getDB():
    ad_f_r = open(ad_file, 'r')
    add_book = serialize.load(ad_f_r)
    return add_book
    ad_f_r.close()

def searchDB(i1):
    pass

def main():
    if argv[1] == 'up':
        add_book = {'Bob M': '0634456788', 'Bill V': '380635433344', 'Willy S': '380632346789'}
        updateDB(add_book)
        print getDB()
    else:
        print "Main"



if __name__ == "__main__":
    main()
