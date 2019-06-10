
login = "ad"
password = "blue"
log = input("Enter login: ")
pas = input("Enter password: ")
max_try = 3
iteretion_try = 1

while max_try != iteretion_try:
    if login == log and password == pas:
        print("you log in")
    elif login == log or password == pas:
        iteretion_try += 1
        print("loggin or passwoed is invalid")
    else:
        iteretion_try += 1
        print("login and password is invalid")