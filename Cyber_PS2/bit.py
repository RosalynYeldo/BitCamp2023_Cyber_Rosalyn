class User:
    def __init__(self, username):
        self.username = username
        self.failed_login_attempts = 0

    def increment_failed_login(self):
        self.failed_login_attempts += 1

    def reset_failed_login(self):
        self.failed_login_attempts = 0

users = {
    "user1": User("user1"),
    "user2": User("user2"),
    # Add more users here
}

def detect_identity_threat(username):
    if username in users:
        user = users[username] 
        exit()
        # user.increment_failed_login()
       # if user.failed_login_attempts >= 3:
        #    print(f"Suspicious login attempts detected for user {username}. Please investigate.")
            # You can take further actions here, such as locking the account or notifying the user/administrator.
        #else:
        #print(f"Failed login attempt for user {username}. Attempts: {user.failed_login_attempts}")
    else:
        user.increment_failed_login()
        print(f"User {username} not found.")
        if user.failed_login_attempts >= 3:
            print(f"Suspicious login attempts detected for user {username}. Please investigate.")
        #else:
         #   print(f"Failed login attempt for user {username}. Attempts: {user.failed_login_attempts}")    

# Consecutive login attempts
for _ in range(3):
    username = input("Enter your username: ")
    detect_identity_threat(username)

# Reset failed login attempts for the user