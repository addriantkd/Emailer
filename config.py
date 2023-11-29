import os

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'invitations')
GUESTS_DIR = os.path.join(BASE_DIR, 'guests')
INBOX_FILE = os.path.join(BASE_DIR, 'inbox.txt')
COWORKERS_LIST = os.path.join(GUESTS_DIR, 'cowokers.txt')
COWORKERS_INVITATION = os.path.join(TEMPLATE_DIR, 'coworkers.txt')
FAMILY_LIST = os.path.join(GUESTS_DIR, 'family.txt')
FAMILY_INVITATION = os.path.join(TEMPLATE_DIR, 'family.txt')
FRIENDS_LIST = os.path.join(GUESTS_DIR, 'friends.txt')
FRIENDS_INVITATION = os.path.join(TEMPLATE_DIR, 'friends.txt')

os.makedirs(GUESTS_DIR, exist_ok=True)

username = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')
my_name = "Adrian Cretu"
