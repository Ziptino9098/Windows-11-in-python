import time


windows_username = ""
windows_password = ""
is_system_stable = True

def install_windows():
    global windows_username, windows_password
    edition = input("Windows 11 edition (home/pro): ").lower()
    print(f"Installing Windows 11 {'Home' if edition == 'home' else 'Pro'}...")
    time.sleep(2)
    print("Installed")
    windows_username = input("Username: ")
    windows_password = input("Password: ")
    print("Password set")

def login():
    password = input("Login password: ")
    if password == windows_password:
        print("Logged in")
    else:
        print("Wrong password")

def install_app(app_name=None):
    if not app_name:
        app_name = input("App name to install: ")
    blocked = app_name.lower() in ["noescape.exe","wannacry.exe","iloveyou.exe","quasarrat.exe","virus.exe"]
    if blocked:
        print("App blocked due to malware")
    else:
        print(f"{app_name} installed")

def delete_file():
    file = input("File to delete: ")
    print(f"{file} deleted")

def delete_app():
    app = input("App to delete: ")
    print(f"{app} deleted")

def change_directory():
    dir = input("Directory to change to: ")
    print(f"Current directory is now {dir}")

def reboot():
    print("Rebooting...")
    time.sleep(2)
    print("Rebooted")

def virus_scan():
    print("Running virus scan...")
    time.sleep(2)
    print("Virus detected and removed")

def app_store():
    app = input("App store install: ")
    install_app(app)

def send_email():
    email = input("Send email to: ")
    if email.lower().startswith("noreply"):
        print("Cannot email noreply addresses")
    else:
        print(f"Email sent to {email}")

def check_status():
    if is_system_stable:
        print("System is stable")
    else:
        print("ERR_CRITICAL_PROCESS_DIED")

def shell():
    while True:
        cmd = input("\nCommand (type help for command options,'exit to quit): ").lower()
        if cmd == "help":
            print("install, del, delapp, cd, reboot, scan, appstore, email, status, exit")
        elif cmd == "install":
            install_app()
        elif cmd == "del":
            delete_file()
        elif cmd == "delapp":
            delete_app()
        elif cmd == "cd":
            change_directory()
        elif cmd == "reboot":
            reboot()
        elif cmd == "scan":
            virus_scan()
        elif cmd == "appstore":
            app_store()
        elif cmd == "email":
            send_email()
        elif cmd == "status":
            check_status()
        elif cmd == "exit":
            print("Exiting cmd")
            break
        else:
            print(f"{cmd} executed successfully")


install_windows()
login()
shell()
