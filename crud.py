import re
import ConfigParser

######## Functions

def search(param):
  db_w = getConf()
  add_book = db_w.getDB()
  for key, val in add_book.items():
    if re.search(param.lower(), key.lower()) or re.search(param, val):
      print key, val


def add(aname, aphone):
  db_w = getConf()
  add_book = db_w.getDB()
  if aname in add_book.keys():
    raise ValueError('Contact exists')
  else:
    add_book[aname] = aphone
    db_w.updateDB(add_book)
  db_contents = db_w.getDB()
  print "DB contents: \n", db_contents.items()


def remove(dname):
  db_w = getConf()
  add_book = db_w.getDB()
  if dname not in add_book:
    raise ValueError('No contact')
  else:
    value = add_book.pop(dname)
    db_w.updateDB(add_book)
    print value + ' deleted'

def getConf():
  config = ConfigParser.ConfigParser()
  config.read(r'D:\python\mypy\config.cfg')
  db_type = config.get('DB_File', 'type')
  if db_type == 'pickle':
    #print 'Pickle'
    db_w = __import__('wFiles_pickle')
    return db_w
  elif db_type == 'csv':
    #print "Csv"
    db_w = __import__('wFiles_csv')
    return db_w

def main():
  pass

if __name__ == "__main__":
  main()
