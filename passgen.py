# IMPORTING MODULES
import random
import array
import time
import sys

# ASKING FOR MAXIMUM PASSWORD LENGTH
MAX_LEN = int(input("\033[1;36;40m [*] Enter Password Length:"))
print('\033[1;36;40m [*] GENERATING PASSWORD...')

# DECLARING ARRAYS
DIGITS = ['0','1','2','3','4','5','6','7','8','9']
LCASE_CHARS = ['a','b','c','d','e','f','g','h','i','j','k','l',
               'm','n','o','p','q','r','s','t','u','v','w','x',
               'y','z']
UCASE_CHARS = ['A','B','C','D','E','F','G''H','I','J','K','L',
               'M','N','O','P','Q','R','S','T','U','V','W','X',
               'Y','Z']
SYMBOLS = ['!','@','#','$','%','&','*','+','-','_','?','/','|',
           ';',':']
# COMBINIG ALL ARRAYS TO FORM ONE ARRAY
COMBINED_LIST = DIGITS + UCASE_CHARS + LCASE_CHARS + SYMBOLS

# RANDOM SELECTION OF AT LEAST ONE CHARACTER FROM ABOVE CHARACTER SET
rand_digit = random.choice(DIGITS)
rand_ucase = random.choice(UCASE_CHARS)
rand_lcase = random.choice(LCASE_CHARS)
rand_symbol = random.choice(SYMBOLS)

# COMBINING SELECTED CHARACTERS
temp_pass = rand_digit + rand_ucase + rand_lcase + rand_symbol

# PASSWORD CREATION STARTS
for x in range(MAX_LEN-4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
    password = password + x
f_pass = password

not_2 = '\033[1;36;40m [+] DONE WITH GENERATING PASSWORD...\n'
for s in not_2:
    sys.stdout.write(s)
    time.sleep(0.2)

print('\033[1;32;40m [+] GENERATED PASSWORD:',f_pass)
