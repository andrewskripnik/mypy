import os
import csv
from sys import argv

ad_file = r'addr_book.csv'
serialize = __import__('csv')

def updateDB(i1):
  u_dict = i1
  with open(ad_file, 'w') as csv_db:
    writer = csv.writer(csv_db)
    for key, val in u_dict.items():
      writer.writerow([key, val])

def getDB():
  with open(ad_file) as csv_db:
    reader = csv.reader(csv_db)
    add_book = dict(reader)
  return add_book

def searchDB(i1):
    pass

def main():
    if argv[1] == 'up':
        add_book = {'Bob C': '0634456788', 'Bill C': '380635433344', 'Willy C': '380632346789'}
        updateDB(add_book)
        print(getDB())
    else:
        print("Main")


if __name__ == "__main__":
    try:
      main()
    except IndexError:
        print("no args")
