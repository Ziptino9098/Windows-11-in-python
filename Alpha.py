
# Restart
restart_set = input("Would you like to restart? (y/n): ")

if restart_set == "y":
    print("Rebooting...")
    time.sleep(3)
    print("Rebooted")

login_passwd_2 = input("Enter Login Password:")

if login_passwd_2 == windows_password:
    print("Logged in")

else:
    print("Wrong password")

appinstall = input("Would you like to install in app?")
if appinstall == "y":
    app2 = input("What app will you install?")
    print(app2 + " will be installed")

else:
    print("app will not be installed")

com2 = input("Enter Command:")
if com2 == "reboot":
    print("Rebooting...")
    time.sleep(3)
    print("Rebooted")
else:
    print("Command Executed Successfully")


command3 = input("Enter Command:")
if command3 == "reboot":
    print("Rebooting...")
    time.sleep(3)
    print("Rebooted")
elif command3 == "del":
    file_to_be_deleted = input("What file do you want to delete?")
    print(file_to_be_deleted + " has been deleted")

elif command3 == "install":
    input("What app do you want to install?")
    time.sleep(3)
    print("Installed")

else:
    print("Command Executed Successfully")


willreboot = input("You need to restart to finish installing the app (y/n): ")
if willreboot == "y":
    print("Rebooting...")
    time.sleep(3)
    print("Rebooted")
else:
    print("System will not be rebooted")

#BSOD Check
if is_system_stable == True:
    print("System is stable")
else:
    print("ERR_CRITICAL_PROCESS_DIED")
    time.sleep(3)
    print("Rebooting...")
    time.sleep(3)
    print("Rebooted")

login_passwd_3 = input("Enter Login Password:")
if login_passwd_3 == windows_password:
    print("Logged in")
else:
    print("Wrong password")



kommand = input("Enter Command: ")
if kommand == "reboot":
    print("Rebooting...")
    time.sleep(3)

elif kommand == "install":
    app67 = input("What app do you want to install?")
    print(app67 + " will be installed")

elif kommand == "del":
    del67 = input("What file do you want to delete?")
    print(del67 + " will be deleted")

elif kommand == "cd":
    dir = input("What dir do you want to change to?")
    print(dir + " is now your current directory")

elif kommand == "delapp":
    delapp67 = input("What app do you want to delete?")
    print(delapp67 + " will be deleted")

else:
    print("Command Executed Successfully")


appstoreapp = input("Welcome to the Windows app store! We have hundreds of apps for you to install! Just type in what to install!")
if appstoreapp == "noescape.exe":
    print("App was blocked due to containing malware")

elif appstoreapp == "wannacry.exe":
    print("App was blocked due to containing malware")

elif appstoreapp == "iloveyou.exe":
    print("App was blocked due to containing malware")

elif appstoreapp == "quasarrat.exe":
    print("App was blocked due to containing malware")

elif appstoreapp == "virus.exe":
    print("App was blocked due to containing malware")

else:
    print(appstoreapp + " has been installed")


send_email_to = input("Who would you like to email?")
if send_email_to == "noreply@gmail.com":
    print("That email is no reply you cannot email them")

else:
    print(send_email_to + " has recived your email")



