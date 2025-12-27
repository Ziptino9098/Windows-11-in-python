import time
#Edition selector
windows_edition = input("What Windows 11 edition will you install? Options are 'home' or 'pro': ").strip().lower()
#Installer
if windows_edition == "home":
    print("You will be installing Windows 11 Home")
else:
    print("You will be installing Windows 11 Pro")

time.sleep(12)
print("Windows 11 has been installed")
#User creation
windows_username = input("Enter windows username:")
print(windows_username + " Will be your username")
windows_password = input("Enter windows password:")
print(windows_password + " Will be your password")
password = input("Enter password to login:")
if password == windows_password:
    print("Logged in")
else:
    print("Wrong password")
app_to_be_installed = input("What app will you install:")
print(app_to_be_installed + " Will be installed")
#Virus protection
app_is_virus = True
protection_reachable = True
if app_is_virus == True:
    print("App was blocked due to containing malware")
elif protection_reachable == False:
    print("App was blocked as malware protection could not be reached")
else:
    print("No threats found in app")

will_scan_run = input("Do you want to run a Virus Detection System Scan? (y/n): ").strip().lower()
if will_scan_run == "y":
    print("Running Virus Detection Scan")
else:
    print("System will not be scanned")

time.sleep(2)

virus_detected = True
if virus_detected == True:
    print("Virus Detected and was removed")

else:
    print("Virus Detected and was removed")


