import pandas as pd

yo=pd.read_csv(r'C:\Users\laksh\Dropbox\My PC (LAPTOP-6UJV2OF2)\Downloads\users.csv\users.csv')


'''def __init__(self, username):
        self.username = username
        self.failed_login_attempts = 0'''

def increment_failed_login(self):
        self.failed_login_attempts += 1

'''def reset_failed_login(self):
        self.failed_login_attempts = 0'''
        
username = input("Enter your username: ")

bunny = yo.to_dict()

if username in bunny:
    #user = bunny[username] 
    exit()
        # user.increment_failed_login()
       # if user.failed_login_attempts >= 3:
        #    print(f"Suspicious login attempts detected for user {username}. Please investigate.")
            # You can take further actions here, such as locking the account or notifying the user/administrator.
        #else:
        #print(f"Failed login attempt for user {username}. Attempts: {user.failed_login_attempts}")
else:
    user = bunny[username]
    increment_failed_login()
    print(f"User {username} not found.")
    if user.failed_login_attempts >= 3:
            print(f"Suspicious login attempts detected for user {username}. Please investigate.")
    else:
        print(username)
        #else:
         #   print(f"Failed login attempt for user {username}. Attempts: {user.failed_login_attempts}")    
'''
# Consecutive login attempts
for _ in range(3):
    username = input("Enter your username: ")
    detect_identity_threat(username)

'''
