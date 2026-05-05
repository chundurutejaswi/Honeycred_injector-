import datetime

def save_log(username, password):
    with open("log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - Attempt: {username} / {password}\n")
