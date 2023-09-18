def authenticate():
    global authenticated
    global userid
    global userpassword
    authenticated=False    
    registered=input("Are you a registered user (y/n)? ")
    if registered=='y':
        userid=input("Enter your user ID: ")
        with open(r'User IDs.txt', 'r') as ids:
            checkid=ids.read()
            if userid in checkid:
                userpassword=input("Enter your password: ")
                with open(r'User Passwords.txt', 'r') as passwords:
                    checkpass=passwords.read()
                    if userpassword in checkpass:
                        print("Successfully logged in!")
                        authenticated=True
                    else:
                        print("Invalid password! You have to restart the program to proceed for security reasons.")
                    passwords.close()
            else:
                print("Invalid username! You have to restart the program to proceed for security reasons.")
                ids.close()
    if registered=='n':
        userid=input("Enter your desired user ID: ")
        with open(r'User IDs.txt', 'r') as ids:
            checkid=ids.read()
            if userid in checkid:
                print("This ID is already taken. Resart the app and try again.")
                ids.close()
            else:
                ids.close()
                with open('User IDs.txt', 'a') as ids:
                    ids.write(userid)
                    ids.write("\n")
                    ids.close()
                userpassword=input("Enter your desired user password: ")
        with open(r'User Passwords.txt', 'r') as passwords:
            checkpass=passwords.read()
            if userpassword in checkpass:
                print("This password is already taken. Resart the app and try again.")
                passwords.close()
            else:
                passwords.close()
                with open('User Passwords.txt', 'a') as passwords:
                    passwords.write(userpassword)
                    passwords.write("\n")
                    passwords.close()
                file=open(userid, 'w')
                file.close()
                print("Now restart the app to login.")

                
                    
                    
            
            