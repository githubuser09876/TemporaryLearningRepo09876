import pikepdf
import os
import shutil

# Load Wordlist
wordlist = input('Enter wordlist: ')
passwords = passwords = [ line.strip() for line in open(wordlist) ]

# Making Directory
try:
    os.mkdir('Decrypted')
except FileExistsError as e:
    pass

# iterate over passwords
def crack(p):
 if ".pdf" in str(p):
  #print('\nOpening: '+str(p))
  print(str(p))
  for password in passwords:
   try:
    # open PDF file
    with pikepdf.open(p, password=password) as pdf:
     # Password decrypted successfully
     print("[+] Password found:", password)
     x=i.split('.pdf')[0]
     y=x+"_DECRYPTED.pdf"
     pdf.save(y)
     shutil.move(y, 'Decrypted')
     pdf.close()
     # break out of the loop
     break
   except pikepdf._qpdf.PasswordError as e:
    # wrong password, just continue in the loop
    continue
 else:
  pass

for i in os.listdir(os.getcwd()):
 crack(i)