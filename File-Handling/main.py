import os, fnmatch 
from colorama import Fore, Back

'''def read_file():
  myfile = open("Stuff/testfile.kenny", "r")
  number = 0
  for record in myfile:
    print(number, "|\n", record, end = "")
    number += 1
  myfile.close()
read_file()'''

print("\n")

def write_to_file():
  xfile = open("Stuff/cats/afile.kenny", "w")

  for number in range(1, 6):
    record = "Henry is a bad cat\n"
    xfile.write(record)

  xfile.close()
write_to_file()

print("\n")

def kenny_file():
  kenny = open("Stuff/KENNY/kenny_was_here.kenny", "r")
  number = 0
  for record in kenny:
    print(number, "|\n", record, end = "")
    number += 1
  kenny.close()
kenny_file()

#                   →  ⇒   ⇄   ↻

for root, dir, files in os.walk("."):
        print(Fore.CYAN, root, Fore.YELLOW)
        print("|>---------------<|\n\n")
        for items in fnmatch.filter(files, "*"):
                print("⇒ " + items)
        print("")