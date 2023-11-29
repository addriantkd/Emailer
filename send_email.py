import sys
import os
from emailer import Emailer
from config import *

def unpack_guests(file_path):
    guests = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if line != '\n':
            line_list = line.rstrip('>\n').split(" <")
        else:
            continue
        guests[line_list[0]] = line_list[1]
    return guests

if __name__ == "__main__":
    my_yahoo = Emailer()        
    if len(sys.argv) > 1:
        list_path = os.path.join(GUESTS_DIR, f'{sys.argv[1]}.txt')
        invitation_path = os.path.join(TEMPLATE_DIR, f'{sys.argv[1]}.txt')
        my_yahoo.send_email(invitation_path, unpack_guests(list_path))
    else:
        my_yahoo.send_email(FAMILY_INVITATION,unpack_guests(FAMILY_LIST))
        my_yahoo.send_email(FRIENDS_INVITATION,unpack_guests(FRIENDS_LIST))
        my_yahoo.send_email(COWORKERS_INVITATION,unpack_guests(COWORKERS_LIST))
    