
from emailer import Emailer

if __name__ == "__main__":
    coworkers = {}
    with open('coworkers_list.txt', 'r') as f:
        name, email = f.readline().rstrip('>\n').split(' <')
        coworkers['name'] = name
        coworkers['email'] = email
         
    my_yahoo = Emailer()
    my_yahoo.send()
        
        
    