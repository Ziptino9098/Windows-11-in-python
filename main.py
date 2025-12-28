import os
import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
import webbrowser

# ---------- GLOBAL VARIABLES ----------
windows_username = "User"
windows_password = "password"
current_dir = os.getcwd()
is_system_stable = True

# ---------- FILE EXPLORER ----------
class FileExplorer:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("File Explorer")
        self.current_dir = current_dir

        self.dir_label = tk.Label(self.root, text=self.current_dir, font=("Arial", 12))
        self.dir_label.pack(pady=5)

        self.listbox = tk.Listbox(self.root, width=60, height=20)
        self.listbox.pack(padx=10, pady=5)
        self.listbox.bind("<Double-Button-1>", self.open_selected_file)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Up", command=self.go_up).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Refresh", command=self.refresh).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="New File", command=self.create_file).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="New Dir", command=self.create_dir).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Delete", command=self.delete_item).grid(row=0, column=4, padx=5)

        self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        self.dir_label.config(text=self.current_dir)
        try:
            for item in os.listdir(self.current_dir):
                self.listbox.insert(tk.END, item)
        except PermissionError:
            messagebox.showerror("Error", "Permission denied.")

    def go_up(self):
        self.current_dir = os.path.dirname(self.current_dir)
        self.refresh()

    def open_selected_file(self, event):
        selection = self.listbox.curselection()
        if selection:
            filename = self.listbox.get(selection[0])
            path = os.path.join(self.current_dir, filename)
            if os.path.isfile(path):
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                self.show_file_content(filename, content)
            elif os.path.isdir(path):
                self.current_dir = path
                self.refresh()

    def show_file_content(self, filename, content):
        win = tk.Toplevel(self.root)
        win.title(filename)
        text_area = scrolledtext.ScrolledText(win, width=80, height=30)
        text_area.pack(padx=10, pady=10)
        text_area.insert(tk.END, content)
        text_area.config(state=tk.DISABLED)

    def create_file(self):
        name = simpledialog.askstring("New File", "Enter file name:")
        if name:
            path = os.path.join(self.current_dir, name)
            open(path, "w").close()
            self.refresh()

    def create_dir(self):
        name = simpledialog.askstring("New Directory", "Enter directory name:")
        if name:
            path = os.path.join(self.current_dir, name)
            os.makedirs(path, exist_ok=True)
            self.refresh()

    def delete_item(self):
        selection = self.listbox.curselection()
        if selection:
            name = self.listbox.get(selection[0])
            path = os.path.join(self.current_dir, name)
            if os.path.isdir(path):
                try:
                    os.rmdir(path)
                except OSError:
                    messagebox.showerror("Error", "Directory not empty.")
            else:
                os.remove(path)
            self.refresh()

# ---------- COMMAND PROMPT ----------
class CommandPrompt:
    installed_apps = []

    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Command Prompt")

        self.text_area = scrolledtext.ScrolledText(self.root, width=80, height=30)
        self.text_area.pack(padx=10, pady=10)
        self.text_area.insert(tk.END, "Mini Command Prompt\nType 'help' for commands\n")
        self.text_area.config(state=tk.DISABLED)

        self.entry = tk.Entry(self.root, width=80)
        self.entry.pack(padx=10, pady=5)
        self.entry.bind("<Return>", self.run_command)

    def run_command(self, event):
        global current_dir, is_system_stable

        cmd = self.entry.get()
        self.entry.delete(0, tk.END)
        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, f"> {cmd}\n")

        parts = cmd.strip().split()
        if not parts:
            self.text_area.config(state=tk.DISABLED)
            return

        command = parts[0].lower()
        args = parts[1:]

        try:
            if command == "help":
                self.text_area.insert(tk.END,
                    "Commands:\n"
                    "ls - list files\n"
                    "cd [dir] - change directory\n"
                    "cat [file] - view file content\n"
                    "touch [file] - create new file\n"
                    "del [file] - delete file\n"
                    "mkdir [dir] - create directory\n"
                    "rmdir [dir] - remove directory\n"
                    "install [app] - install an app\n"
                    "delapp [app] - delete an installed app\n"
                    "scan - run virus scan\n"
                    "status - check system stability\n"
                    "reboot - reboot system\n"
                    "exit - close command prompt\n"
                )
            elif command == "ls":
                for f in os.listdir(current_dir):
                    self.text_area.insert(tk.END, f + "\n")
            elif command == "cd":
                if args:
                    path = args[0]
                    new_path = os.path.join(current_dir, path)
                    if os.path.isdir(new_path):
                        current_dir = os.path.abspath(new_path)
                        self.text_area.insert(tk.END, f"Changed directory to {current_dir}\n")
                    else:
                        self.text_area.insert(tk.END, "Directory not found\n")
                else:
                    self.text_area.insert(tk.END, current_dir + "\n")
            elif command == "cat":
                if args:
                    path = os.path.join(current_dir, args[0])
                    if os.path.isfile(path):
                        with open(path, "r", encoding="utf-8", errors="ignore") as f:
                            self.text_area.insert(tk.END, f.read() + "\n")
                    else:
                        self.text_area.insert(tk.END, "File not found\n")
            elif command == "touch":
                if args:
                    path = os.path.join(current_dir, args[0])
                    open(path, "w").close()
                    self.text_area.insert(tk.END, f"{args[0]} created\n")
            elif command == "del":
                if args:
                    path = os.path.join(current_dir, args[0])
                    if os.path.isfile(path):
                        os.remove(path)
                        self.text_area.insert(tk.END, f"{args[0]} deleted\n")
                    else:
                        self.text_area.insert(tk.END, "File not found\n")
            elif command == "mkdir":
                if args:
                    path = os.path.join(current_dir, args[0])
                    os.makedirs(path, exist_ok=True)
                    self.text_area.insert(tk.END, f"{args[0]} created\n")
            elif command == "rmdir":
                if args:
                    path = os.path.join(current_dir, args[0])
                    try:
                        os.rmdir(path)
                        self.text_area.insert(tk.END, f"{args[0]} removed\n")
                    except OSError:
                        self.text_area.insert(tk.END, "Directory not empty or not found\n")
            elif command == "install":
                if args:
                    app = args[0]
                    if app.lower() in ["noescape.exe", "wannacry.exe", "iloveyou.exe", "quasarrat.exe", "virus.exe"]:
                        self.text_area.insert(tk.END, "App blocked due to malware!\n")
                    else:
                        self.installed_apps.append(app)
                        self.text_area.insert(tk.END, f"{app} installed successfully\n")
                else:
                    self.text_area.insert(tk.END, "Specify app to install\n")
            elif command == "delapp":
                if args:
                    app = args[0]
                    if app in self.installed_apps:
                        self.installed_apps.remove(app)
                        self.text_area.insert(tk.END, f"{app} deleted\n")
                    else:
                        self.text_area.insert(tk.END, "App not installed\n")
            elif command == "scan":
                self.text_area.insert(tk.END, "Running virus scan...\nVirus detected and removed\n")
            elif command == "status":
                if is_system_stable:
                    self.text_area.insert(tk.END, "System is stable\n")
                else:
                    self.text_area.insert(tk.END, "ERR_CRITICAL_PROCESS_DIED\n")
            elif command == "reboot":
                self.text_area.insert(tk.END, "Rebooting system...\nSystem rebooted\n")
            elif command == "exit":
                self.root.destroy()
            else:
                self.text_area.insert(tk.END, f"{cmd} executed\n")
        except Exception as e:
            self.text_area.insert(tk.END, f"Error: {str(e)}\n")

        self.text_area.config(state=tk.DISABLED)
        self.text_area.see(tk.END)

# ---------- WEB BROWSER ----------
class WebBrowser:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Web Browser")

        tk.Label(self.root, text="Enter website URL:").pack(pady=5)
        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.pack(pady=5)
        self.url_entry.insert(0, "https://www.google.com")

        tk.Button(self.root, text="Go", command=self.open_web).pack(pady=5)

    def open_web(self):
        url = self.url_entry.get()
        if not url.startswith("http"):
            url = "https://" + url
        webbrowser.open(url)

# ---------- DESKTOP ----------
def main_desktop():
    root = tk.Tk()
    root.title("Mini Windows OS")

    tk.Label(root, text=f"Welcome {windows_username}!", font=("Arial", 16)).pack(pady=10)
    tk.Label(root, text="Select an app to open:", font=("Arial", 12)).pack(pady=5)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="File Explorer", width=20, height=2, command=lambda: FileExplorer(root)).grid(row=0, column=0, padx=10)
    tk.Button(btn_frame, text="Command Prompt", width=20, height=2, command=lambda: CommandPrompt(root)).grid(row=0, column=1, padx=10)
    tk.Button(btn_frame, text="Web Browser", width=20, height=2, command=lambda: WebBrowser(root)).grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

# ---------- LOGIN GUI ----------
def login_gui():
    login_root = tk.Tk()
    login_root.title("Mini Windows OS Login")
    login_root.geometry("300x200")

    tk.Label(login_root, text="Username:").pack(pady=5)
    username_entry = tk.Entry(login_root)
    username_entry.pack(pady=5)
    username_entry.insert(0, windows_username)

    tk.Label(login_root, text="Password:").pack(pady=5)
    password_entry = tk.Entry(login_root, show="*")
    password_entry.pack(pady=5)

    def attempt_login():
        global windows_username, windows_password
        username = username_entry.get()
        password = password_entry.get()
        if username == windows_username and password == windows_password:
            messagebox.showinfo("Login", "Logged in successfully!")
            login_root.destroy()
            main_desktop()
        else:
            messagebox.showerror("Login", "Incorrect username or password!")

    tk.Button(login_root, text="Login", command=attempt_login).pack(pady=10)
    login_root.mainloop()

# ---------- RUN OS ----------
if __name__ == "__main__":
    # Setup credentials
    root = tk.Tk()
    root.withdraw()  # hide temporary root
    windows_username = simpledialog.askstring("Setup", "Set username:", initialvalue="User")
    windows_password = simpledialog.askstring("Setup", "Set password:", show="*")
    root.destroy()
    login_gui()
