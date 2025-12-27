import time

windows_edition = input("What Windows 11 edition will you install? Options are 'home' or 'pro': ").strip().lower()

if windows_edition == "home":
    print("You will be installing Windows 11 Home")
else:
    print("You will be installing Windows 11 Pro")

time.sleep(12)
print("Windows 11 has been installed")
windows_username = input("Enter windows username:")
print(windows_username + " Will be your username")
windows_password = input("Enter windows password:")
print(windows_password + " Will be your password")
password = input("Enter password to login:")
if password == windows_password:
    print("Logged in")
