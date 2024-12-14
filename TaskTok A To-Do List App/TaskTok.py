import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
import bcrypt
import re

def connect():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root", 
            password="",  
            database="tasktok_db"  
        )
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

class LoginRegister:
    def __init__(self, master):
        self.master = master
        self.master.title("TaskTok - Login/Register")
        self.master.geometry("700x700")
        self.master.resizable(False, False)

        self.frame = ctk.CTkFrame(master, corner_radius=10, bg_color="#F0F8FF")
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.header_label = ctk.CTkLabel(
            self.frame,
            text="TASKTOK",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.header_label.pack(pady=20)

        self.subheader_label = ctk.CTkLabel(
            self.frame,
            text="Organize your tasks effectively",
            font=ctk.CTkFont(size=16),
            text_color="#808080"
        )
        self.subheader_label.pack(pady=(0, 20))

        self.login_button = ctk.CTkButton(
            self.frame,
            text="Login",
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self.login_screen
        )
        self.login_button.pack(pady=20)

        self.register_button = ctk.CTkButton(
            self.frame,
            text="Register",
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self.register_screen
        )
        self.register_button.pack()

        self.exit_button = ctk.CTkButton(
            self.frame,
            text="Exit",
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self.master.quit  
        )
        self.exit_button.pack(pady=20)

    def login_screen(self):
        self.frame.destroy()
        Login(self.master)

    def register_screen(self):
        self.frame.destroy()
        Register(self.master)

class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("TaskTok - Login")
        self.master.geometry("700x700")

        self.frame = ctk.CTkFrame(master, corner_radius=10, bg_color="#F0F8FF")
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.header_label = ctk.CTkLabel(self.frame, text="Login", font=ctk.CTkFont(size=24, weight="bold"))
        self.header_label.pack(pady=20)

        self.identifier = ctk.StringVar()
        self.identifier_label = ctk.CTkLabel(self.frame, text="Email/Username", font=ctk.CTkFont(size=14))
        self.identifier_label.pack(pady=(20, 5))
        self.identifier_entry = ctk.CTkEntry(self.frame, textvariable=self.identifier, width=300)
        self.identifier_entry.pack()

        self.password = ctk.StringVar()
        self.password_label = ctk.CTkLabel(self.frame, text="Password", font=ctk.CTkFont(size=14))
        self.password_label.pack(pady=(20, 5))
        self.password_entry = ctk.CTkEntry(self.frame, textvariable=self.password, width=300, show="*")
        self.password_entry.pack()

        self.login_button = ctk.CTkButton(self.frame, text="Login", command=self.login, font=ctk.CTkFont(size=14, weight="bold"))
        self.login_button.pack(pady=20)

        self.back_button = ctk.CTkButton(self.frame, text="Back", command=self.back, font=ctk.CTkFont(size=14, weight="bold"))
        self.back_button.pack()

    def login(self):
        con = connect()
        if con is None:
            return

        cur = con.cursor()
        try:
            # Retrieve user by exact match for username or email
            cur.execute("SELECT id, username, email, password FROM users WHERE (BINARY username = %s OR BINARY email = %s)", 
                        (self.identifier.get(), self.identifier.get()))
            row = cur.fetchone()

            if row:
                user_id, username, email, hashed_password = row
                if bcrypt.checkpw(self.password.get().encode('utf-8'), hashed_password.encode('utf-8')):
                    self.frame.destroy()
                    Dashboard(self.master, user_id)
                else:
                    messagebox.showerror("Error", "Invalid password!")
            else:
                messagebox.showerror("Error", "Username or email does not match!")
        finally:
            con.close()


    def back(self):
        self.frame.destroy()
        LoginRegister(self.master)

class Register:
    def __init__(self, master):
        self.master = master
        self.master.title("TaskTok - Register")
        self.master.geometry("700x700")

        self.frame = ctk.CTkFrame(master, corner_radius=10, bg_color="#F0F8FF")
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.header_label = ctk.CTkLabel(self.frame, text="Register", font=ctk.CTkFont(size=24, weight="bold"))
        self.header_label.pack(pady=20)

        self.username = ctk.StringVar()
        self.username_label = ctk.CTkLabel(self.frame, text="Username", font=ctk.CTkFont(size=14))
        self.username_label.pack(pady=(20, 5))
        self.username_entry = ctk.CTkEntry(self.frame, textvariable=self.username, width=300)
        self.username_entry.pack()

        self.email = ctk.StringVar()
        self.email_label = ctk.CTkLabel(self.frame, text="Email", font=ctk.CTkFont(size=14))
        self.email_label.pack(pady=(20, 5))
        self.email_entry = ctk.CTkEntry(self.frame, textvariable=self.email, width=300)
        self.email_entry.pack()

        self.password = ctk.StringVar()
        self.password_label = ctk.CTkLabel(self.frame, text="Password", font=ctk.CTkFont(size=14))
        self.password_label.pack(pady=(20, 5))
        self.password_entry = ctk.CTkEntry(self.frame, textvariable=self.password, width=300, show="*")
        self.password_entry.pack()

        self.register_button = ctk.CTkButton(self.frame, text="Register", command=self.register, font=ctk.CTkFont(size=14, weight="bold"))
        self.register_button.pack(pady=20)

        self.back_button = ctk.CTkButton(self.frame, text="Back", command=self.back, font=ctk.CTkFont(size=14, weight="bold"))
        self.back_button.pack()

    def register(self):
        if not is_valid_email(self.email.get()):
            messagebox.showerror("Error", "Invalid email address!")
            return

        con = connect()
        if con is None:
            return

        cur = con.cursor()
        try:
            hashed_password = bcrypt.hashpw(self.password.get().encode('utf-8'), bcrypt.gensalt())
            cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                        (self.username.get(), self.email.get(), hashed_password.decode('utf-8')))
            con.commit()
            messagebox.showinfo("Success", "Registration successful!")
            self.back()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            con.close()

    def back(self):
        self.frame.destroy()
        LoginRegister(self.master)

class Dashboard:
    def __init__(self, master, user_id):
        self.master = master
        self.user_id = user_id
        self.master.title("Menu")
        self.master.geometry("700x700")
        self.master.resizable(False, False)

        self.frame = ctk.CTkFrame(master, corner_radius=10, bg_color="#F0F8FF")
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.header_label = ctk.CTkLabel(self.frame, text="Menu", font=ctk.CTkFont(size=24, weight="bold"))
        self.header_label.pack(pady=20)

        button_font = ctk.CTkFont(size=16, weight="bold")
        self.add_task_button = ctk.CTkButton(self.frame, text="Add Task", command=self.add_task, font=button_font, width=250)
        self.add_task_button.pack(pady=10, padx=40)

        self.view_tasks_button = ctk.CTkButton(self.frame, text="View Tasks", command=self.view_tasks, font=button_font, width=250)
        self.view_tasks_button.pack(pady=10, padx=40)

        self.account_settings_button = ctk.CTkButton(self.frame, text="Account Settings", command=self.account_settings, font=button_font, width=250)
        self.account_settings_button.pack(pady=10, padx=40)

        self.logout_button = ctk.CTkButton(self.frame, text="Logout", command=self.logout, font=button_font, width=250)
        self.logout_button.pack(pady=10, padx=40)

        self.exit_button = ctk.CTkButton(
            self.frame,
            text="Exit",
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self.master.quit  
        )
        self.exit_button.pack(pady=20)

    def add_task(self):
        self.frame.destroy()
        ViewTasks(self.master, self.user_id, action="add")

    def view_tasks(self):
        self.frame.destroy()
        ViewTasks(self.master, self.user_id, action="view")

    def account_settings(self):
        self.frame.destroy()
        AccountSettings(self.master, self.user_id)

    def logout(self):
        self.frame.destroy()
        LoginRegister(self.master)


class ViewTasks:
    def __init__(self, master, user_id, action):
        self.master = master
        self.user_id = user_id
        self.action = action
        self.master.title("View Tasks")
        self.master.geometry("700x700")

        self.frame = ctk.CTkFrame(master, corner_radius=10, bg_color="#F0F8FF")
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.header_label = ctk.CTkLabel(self.frame, text="View Tasks", font=ctk.CTkFont(size=24, weight="bold"))
        self.header_label.pack(pady=20)

        self.tasks_listbox = tk.Listbox(self.frame, height=15, width=60, font=("Arial", 14), bg="#4C4C4C", selectbackground="#4C4C4C", fg="white")  
        self.tasks_listbox.pack(pady=20)

        self.back_button = ctk.CTkButton(self.frame, text="Back", command=self.back, font=ctk.CTkFont(size=14, weight="bold"))
        self.back_button.pack(pady=10)

        if self.action == "add":
            self.task_name = ctk.StringVar()
            self.task_label = ctk.CTkLabel(self.frame, text="Add Your Task", font=ctk.CTkFont(size=16, weight="bold", family="Arial"))
            self.task_label.pack(pady=(20, 5))
            self.task_entry = ctk.CTkEntry(self.frame, textvariable=self.task_name, width=300)
            self.task_entry.pack()

            self.add_button = ctk.CTkButton(self.frame, text="Add Task", command=self.save_task, font=ctk.CTkFont(size=16, weight="bold"))
            self.add_button.pack(pady=20)

        elif self.action == "view":
            self.load_tasks()
            self.complete_button = ctk.CTkButton(self.frame, text="Complete", command=self.complete_task, font=ctk.CTkFont(size=16, weight="bold"))
            self.complete_button.pack(pady=10)

            self.redo_button = ctk.CTkButton(self.frame, text="Redo", command=self.redo_task, font=ctk.CTkFont(size=16, weight="bold"))
            self.redo_button.pack(pady=10)

            self.delete_button = ctk.CTkButton(self.frame, text="Delete", command=self.delete_task, font=ctk.CTkFont(size=16, weight="bold"))
            self.delete_button.pack(pady=10)

    def save_task(self):
        con = connect()
        if con is None:
            return

        cur = con.cursor()
        try:
            task_name = self.task_name.get()
            cur.execute("INSERT INTO tasks (user_id, name, status) VALUES (%s, %s, 'pending')", 
                        (self.user_id, task_name))
            con.commit()
            messagebox.showinfo("Success", "Task added successfully!")
            
            self.load_tasks() 
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            con.close()

    def load_tasks(self):
        self.tasks_listbox.delete(0, tk.END)

        con = connect()
        if con is None:
            return

        cur = con.cursor()
        try:
            cur.execute("SELECT id, name, status FROM tasks WHERE user_id = %s", (self.user_id,))
            rows = cur.fetchall()
            for row in rows:
                task_id, task_name, status = row
                display_text = f"{task_name} - {status.capitalize()}"
                self.tasks_listbox.insert(tk.END, (task_id, display_text))
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            con.close()
    
    def complete_task(self):
        selected_task = self.tasks_listbox.curselection()
        if not selected_task:
            messagebox.showwarning("Warning", "Please select a task.")
            return

        task_id = self.tasks_listbox.get(selected_task[0])[0]
        con = connect()
        if con is None:
            return

        cur = con.cursor()
        try:
            cur.execute("UPDATE tasks SET status = 'completed' WHERE id = %s", (task_id,))
            con.commit()
            messagebox.showinfo("Success", "Task marked as completed!")
            self.load_tasks() 
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            con.close()
    
    def redo_task(self):
        selected_task = self.tasks_listbox.curselection()
        if not selected_task:
            messagebox.showwarning("Warning", "Please select a task.")
            return

        task_id = self.tasks_listbox.get(selected_task[0])[0]
        con = connect()
        if con is None:
            return

        cur = con.cursor()
        try:
            cur.execute("UPDATE tasks SET status = 'pending' WHERE id = %s", (task_id,))
            con.commit()
            messagebox.showinfo("Success", "Task marked as pending!")
            self.load_tasks()  
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            con.close()
    
    def delete_task(self):
        selected_task = self.tasks_listbox.curselection()
        if not selected_task:
            messagebox.showwarning("Warning", "Please select a task.")
            return

        task_id = self.tasks_listbox.get(selected_task[0])[0]
        con = connect()
        if con is None:
            return

        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this task?")
        if confirm:
            cur = con.cursor()
            try:
                cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
                con.commit()
                messagebox.showinfo("Success", "Task deleted successfully!")
                self.load_tasks() 
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                con.close()

    def back(self):
        self.frame.destroy()
        Dashboard(self.master, self.user_id)  

    def back(self):
        self.frame.destroy()
        Dashboard(self.master, self.user_id)  


class AccountSettings:
    def __init__(self, master, user_id):
        self.master = master
        self.user_id = user_id
        self.master.title("Account Settings")
        self.master.geometry("700x700")

        self.frame = ctk.CTkFrame(master, corner_radius=10, bg_color="#F0F8FF")
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.header_label = ctk.CTkLabel(self.frame, text="Account Settings", font=ctk.CTkFont(size=24, weight="bold"))
        self.header_label.pack(pady=20)

        self.username = ctk.StringVar()
        self.email = ctk.StringVar()
        self.get_user_data()

        self.username_label = ctk.CTkLabel(self.frame, text="Username", font=ctk.CTkFont(size=14))
        self.username_label.pack(pady=(20, 5))
        self.username_entry = ctk.CTkEntry(self.frame, textvariable=self.username, width=300)
        self.username_entry.pack()

        self.email_label = ctk.CTkLabel(self.frame, text="Email", font=ctk.CTkFont(size=14))
        self.email_label.pack(pady=(20, 5))
        self.email_entry = ctk.CTkEntry(self.frame, textvariable=self.email, width=300)
        self.email_entry.pack()

              
        self.button_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.button_frame.pack(pady=10)  

        self.update_button = ctk.CTkButton(
            self.button_frame,
            text="Update Account",
            command=self.update_account,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.update_button.grid(row=0, column=0, padx=10)  

        self.delete_button = ctk.CTkButton(
            self.button_frame,
            text="Delete Account",
            command=self.delete_account,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#FF6347"  
        )
        self.delete_button.grid(row=0, column=1, padx=10) 


        self.back_button = ctk.CTkButton(self.frame, text="Back", command=self.back, font=ctk.CTkFont(size=14, weight="bold"))
        self.back_button.pack()

    def get_user_data(self):
        con = connect()
        if con is None:
            return

        cur = con.cursor()
        try:
            cur.execute("SELECT username, email FROM users WHERE id = %s", (self.user_id,))
            row = cur.fetchone()
            if row:
                self.username.set(row[0])
                self.email.set(row[1])
        finally:
            con.close()

    def update_account(self):
        if not is_valid_email(self.email.get()):
            messagebox.showerror("Error", "Invalid email address!")
            return

        con = connect()
        if con is None:
            return

        cur = con.cursor()
        try:
            cur.execute("UPDATE users SET username = %s, email = %s WHERE id = %s", 
                        (self.username.get(), self.email.get(), self.user_id))
            con.commit()
            messagebox.showinfo("Success", "Account updated successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            con.close()

    def delete_account(self):
        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete your account?")
        if confirm:
            con = connect()
            if con is None:
                return

            cur = con.cursor()
            try:
                cur.execute("DELETE FROM users WHERE id = %s", (self.user_id,))
                con.commit()
                messagebox.showinfo("Success", "Account deleted successfully!")
                self.frame.destroy()  
                LoginRegister(self.master) 
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                con.close()


    def back(self):
        self.frame.destroy()
        Dashboard(self.master, self.user_id)

if __name__ == "__main__":
    root = ctk.CTk()
    LoginRegister(root)
    root.mainloop()
