For this project to work, I generated a key-password from yahoo mail to connect successfully to the server,
then I created environment variables to secure my credentials.

The project is based on the idea of sending the invitations for a weeding by email.

PART I - reading inbox
1. First of all, I got the guests list from the inbox looking for an email by its subject.
2. Second, I chose to store this email in a txt file named "inbox.txt" for future works.
3. The guests are divided into 3 groups (friends, family and coworkers) so I do the same with the files, 
I created 3 of them with name-email of each of guest.

> python -i .\read_email.py *SUBJECT*

PART II - sending emails
4.I decided to send the invitation email according to 3 different templates depending on the group they belong to.
5.Formatted the templates by every guest name.
6.Finnaly, I sent the emails for all the groups or for the group I chose to.

> python -i .\send_email.py *GROUP_OF_GUESTS*