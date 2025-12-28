#This is a mimic of Windows 11 installer and command prompt to show a basic os coded in python
import time

# Edition selector
windows_edition = input(
    "What Windows 11 edition will you install? Options are 'home' or 'pro': ")

# Installer
if windows_edition == "home":
    print("You will be installing Windows 11 Home")
else:
    print("You will be installing Windows 11 Pro")

time.sleep(2)
print("Windows 11 has been installed")

# User creation
windows_username = input("Enter windows username: ")
print(windows_username + " will be your username")

windows_password = input("Enter windows password: ")
print("Password set")

password = input("Enter password to login: ")
if password == windows_password:
    print("Logged in")
else:
    print("Wrong password")

# App install
app_to_be_installed = input("What app will you install: ")
print(app_to_be_installed + " will be installed")

# Virus protection
app_is_virus = True
protection_reachable = True

if app_is_virus:
    print("App was blocked due to containing malware")
elif not protection_reachable:
    print("App was blocked as malware protection could not be reached")
else:
    print("No threats found in app")

# Scan prompt
will_scan_run = input(
    "Do you want to run a Virus Detection System Scan? (y/n): ")

if will_scan_run == "y":
    print("Running Virus Detection Scan")
else:
    print("System will not be scanned")

time.sleep(2)

virus_detected = True
if virus_detected:
    print("Virus detected and removed")
else:
    print("No viruses found")

# System stability
is_system_stable = True

if is_system_stable:
    print("System is stable")
else:
    print("System Crash: ERR_CRITICAL_PROCESS_DIED")

# Command execution
command = input("Enter Command: ")
print(command + " was executed successfully")

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




