"""
This module provides functionalities to search, add, and remove contacts from an address book.
"""

from crud import search, add, remove

act = input('Choose action: \nsearch \nadd \ndelete \ngetDB \n')
add_book = {}

######## Main ########
def main():
  if act.lower() in ['se', 'sea', 'sear', 'searc', 'search']:
    sname = input('Name for search please: ')
    search(sname)
  elif act.lower() == 'add':
    aname = input('Name for update please: ')
    aphone = input('Phone for update please: ')
    try:
      add(aname, aphone)
    except ValueError:
      print('Contact exists')
  elif act.lower() in ['delete','del']:
    dname = input('Exact name for deletion please: ')
    try:
      remove(dname)
    except ValueError:
      print('No such contact')
  elif act == 'getDB':
    try:
      print("getDB()")
    except ValueError:
      print(ValueError)
  else: print("Choose action: se[arch], add, del[ete], getDB ")


if __name__ == "__main__":
  main()
