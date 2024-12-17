from crud import search, add, remove

act = raw_input('Choose action: \nsearch \nadd \ndelete \ngetDB \n')
add_book = {}


######## Main
def main():
  if act.lower() in ['se', 'sea', 'sear', 'searc', 'search']:
      sname = raw_input('Name for search please: ')
      search(sname)

  elif act.lower() == 'add':
      aname = raw_input('Name for update please: ')
      aphone = raw_input('Phone for update please: ')
      try:
          add(aname, aphone)
      except ValueError:
          print 'Contact exists'

  elif act.lower() in ['delete','del']:
      dname = raw_input('Exact name for deletion please: ')
      try:
          remove(dname)
      except ValueError:
          print 'No such contact'

  elif act == 'getDB':
      try:
          print "getDB()"
      except ValueError:
          print ValueError

  else: print "Choose action: se[arch], add, del[ete], getDB "


if __name__ == "__main__":
    main()

