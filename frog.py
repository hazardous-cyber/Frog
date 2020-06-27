#!/usrbin/env python3

# importbuilt-in libraries
imoprt os
import sys
import random
import string

# function to create password
def creat_password():
    chrs = string.ascii_letters + string.digits + '!@#$%^&*()?'
    password = ''.join(random.sample(chrs,15))
    print(password)
    return password
    
# function to add user
def add_user():
    if not 'SUDO_UID' in os.environ.keys():
        print('[x] This script requires super-user privileges (sudo).')
        exit()
        
    username = 'frog'
    
    try:
        addUser = 'adduser --disabled-login --gecos "" %s' % username
        os.system(addUser)
        
    except:
        print('Failed to add user.')
        
# function to set password for new user
def set_password():
    genPassword = create_password()
    username = frog
    
    try:
        makeFile = 'echo "%s:%s" > passwords.txt' % (username, genPassword)
        os.system(makeFile)
        changePassword = 'chpasswd < passwords.txt'
        os.system(changePassword)
        
    except:
        print('Failed to make file')
        sys.exit(1)
        
# call functions to add user and set password
add_user()
set_password()
