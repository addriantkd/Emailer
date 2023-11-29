import os
import sys
from config import INBOX_FILE, FAMILY_LIST, FRIENDS_LIST, COWORKERS_LIST
from emailer import Emailer

def set_guests_type():
    with open(INBOX_FILE, 'r') as file:
        for line in file.readlines():
            if "Family" in line:
                with open(FAMILY_LIST, 'w') as f:
                    f.write(">\n".join(line.split(':')[1].split(">")))
            elif "Friends" in line:
                with open(FRIENDS_LIST, 'w') as f:
                    f.write(">\n".join(line.split(':')[1].split(">")))
            elif "Coworkers" in line:
                with open(COWORKERS_LIST, 'w') as f:
                    f.write(">\n".join(line.split(':')[1].split(">")))
    print(f"Guest list ordered and stored in {os.path.dirname(FAMILY_LIST)}")
            
if __name__ == '__main__':
    my_yahoo = Emailer()
    if len(sys.argv) > 1:
        my_yahoo.read_email(sys.argv[1])
    set_guests_type()