import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from data_persistence import DataPersistence

# Color scheme
BG_COLOR = "#f0f0f0"
BUTTON_COLOR = "#4CAF50"
BUTTON_HOVER = "#45a049"
BUTTON_DELETE = "#f44336"
TEXT_COLOR = "#333333"
TITLE_COLOR = "#2c3e50"

class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False

    def mark_as_read(self):
        self.read = True

    def display_full_email(self):
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self):
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

class Inbox:
    def __init__(self):
        self.emails = []

    def receive_email(self, email):
        self.emails.append(email)

    def list_emails(self):
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    def read_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        self.emails[actual_index].display_full_email()

    def delete_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        del self.emails[actual_index]
        print('Email deleted.\n')

class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index):
        self.inbox.read_email(index)

    def delete_email(self, index):
        self.inbox.delete_email(index)

def main():
    tory = User('Tory')
    ramy = User('Ramy')        
    
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    # Ramy checks inbox
    ramy.check_inbox()

    # Ramy reads first email
    ramy.read_email(1)

    # Ramy deletes first email
    ramy.delete_email(1)

    # Ramy checks inbox again
    ramy.check_inbox()

class EmailSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Email System")
        self.root.geometry("800x600")
        self.root.configure(bg=BG_COLOR)
        self.persistence = DataPersistence()
        
        # Dictionary to store users
        self.users = {}
        self.current_user = None
        self.current_inbox_emails = []
        
        # Configure styles
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', font=('Arial', 10))
        
        # Create main frame
        self.main_frame = tk.Frame(root, bg=BG_COLOR)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Title frame
        title_frame = tk.Frame(self.main_frame, bg=TITLE_COLOR)
        title_frame.pack(fill=tk.X, padx=0, pady=(0, 15))
        
        title_label = tk.Label(title_frame, text="✉️  Email System", 
                              font=("Arial", 20, "bold"), bg=TITLE_COLOR, fg="white")
        title_label.pack(pady=15)
        
        # Button frame - organized in a grid
        button_frame = tk.Frame(self.main_frame, bg=BG_COLOR)
        button_frame.pack(pady=10, fill=tk.X)
        
        # Create styled buttons
        self.create_button(button_frame, "Create User", self.create_user, 0, 0, BUTTON_COLOR)
        self.create_button(button_frame, "Send Email", self.send_email, 0, 1, BUTTON_COLOR)
        self.create_button(button_frame, "Check Inbox", self.check_inbox, 0, 2, BUTTON_COLOR)
        self.create_button(button_frame, "Read Email", self.read_email_gui, 1, 0, "#2196F3")
        self.create_button(button_frame, "Delete Email", self.delete_email_gui, 1, 1, BUTTON_DELETE)
        self.create_button(button_frame, "Clear Display", self.clear_display, 1, 2, "#FF9800")
        
        # Status frame
        status_frame = tk.Frame(self.main_frame, bg="#e0e0e0")
        status_frame.pack(fill=tk.X, pady=(10, 0), padx=0)
        
        self.status_label = tk.Label(status_frame, text="Status: Ready", 
                                    font=("Arial", 9), bg="#e0e0e0", fg=TEXT_COLOR)
        self.status_label.pack(pady=8, padx=10, anchor=tk.W)
        
        # Display area with scrollbar
        display_frame = tk.Frame(self.main_frame, bg=BG_COLOR)
        display_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        scrollbar = tk.Scrollbar(display_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.display_text = tk.Text(display_frame, height=20, width=80, 
                                   yscrollcommand=scrollbar.set,
                                   font=("Monaco", 10), bg="white", fg=TEXT_COLOR,
                                   wrap=tk.WORD, relief=tk.SUNKEN, borderwidth=2)
        self.display_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.display_text.yview)
        
        # Welcome message
        self.log_to_display("Welcome to Email System! 📧\n")
        self.log_to_display("=" * 70)
        self.log_to_display("Commands available:")
        self.log_to_display("1. Create User - Set up a new user account")
        self.log_to_display("2. Send Email - Send email between users")
        self.log_to_display("3. Check Inbox - View all emails for a user")
        self.log_to_display("4. Read Email - View full email content")
        self.log_to_display("5. Delete Email - Remove an email from inbox")
        self.log_to_display("=" * 70 + "\n")
    
    def create_button(self, parent, text, command, row, col, color):
        """Create a styled button"""
        btn = tk.Button(parent, text=text, command=command, 
                       bg=color, fg="white", font=("Arial", 10, "bold"),
                       padx=12, pady=8, relief=tk.RAISED, cursor="hand2",
                       activebackground="#555555", activeforeground="white")
        btn.grid(row=row, column=col, padx=8, pady=5, sticky="ew")
        parent.grid_columnconfigure(col, weight=1)
    
    def update_status(self, message):
        """Update status bar"""
        self.status_label.config(text=f"Status: {message}")
    
    def log_to_display(self, message):
        """Add message to display area"""
        self.display_text.insert(tk.END, message + "\n")
        self.display_text.see(tk.END)
    
    def clear_display(self):
        """Clear the display area"""
        self.display_text.delete(1.0, tk.END)
        self.update_status("Display cleared")
    
    def create_user(self):
        """Create a new user"""
        name = simpledialog.askstring("Create User", "Enter username:")
        if name:
            if name not in self.users:
                self.users[name] = User(name)
                self.log_to_display(f"✅ User '{name}' created successfully!")
                self.persistence.save_data(self.users)
                self.update_status(f"User '{name}' created")
            else:
                messagebox.showerror("Error", f"User '{name}' already exists!")
                self.update_status("Error: User already exists")
    
    def send_email(self):
        """Send email between users"""
        if len(self.users) < 2:
            messagebox.showerror("Error", "Need at least 2 users to send email!")
            self.update_status("Error: Need 2+ users")
            return
        
        sender_name = simpledialog.askstring("Send Email", "Enter sender name:")
        if not sender_name or sender_name not in self.users:
            messagebox.showerror("Error", "Sender not found!")
            self.update_status("Error: Sender not found")
            return
        
        receiver_name = simpledialog.askstring("Send Email", "Enter receiver name:")
        if not receiver_name or receiver_name not in self.users:
            messagebox.showerror("Error", "Receiver not found!")
            self.update_status("Error: Receiver not found")
            return
        
        subject = simpledialog.askstring("Send Email", "Enter subject:")
        if not subject:
            return
        
        body = simpledialog.askstring("Send Email", "Enter message body:", parent=self.root)
        if not body:
            return
        
        self.users[sender_name].send_email(self.users[receiver_name], subject, body)
        self.log_to_display(f"✅ Email sent from {sender_name} to {receiver_name}!")
        self.persistence.save_data(self.users)
        self.update_status(f"Email sent: {sender_name} → {receiver_name}")
    
    def check_inbox(self):
        """Check user's inbox"""
        if not self.users:
            messagebox.showerror("Error", "No users created!")
            self.update_status("Error: No users")
            return
        
        user_name = simpledialog.askstring("Check Inbox", "Enter username:")
        if not user_name or user_name not in self.users:
            messagebox.showerror("Error", "User not found!")
            self.update_status("Error: User not found")
            return
        
        self.current_user = user_name
        self.current_inbox_emails = self.users[user_name].inbox.emails
        
        self.clear_display()
        self.log_to_display(f"\n{'=' * 70}")
        self.log_to_display(f"📬 {user_name}'s Inbox")
        self.log_to_display(f"{'=' * 70}\n")
        
        inbox = self.users[user_name].inbox
        if not inbox.emails:
            self.log_to_display("Your inbox is empty.\n")
        else:
            self.log_to_display(f"Total emails: {len(inbox.emails)}\n")
            for i, email in enumerate(inbox.emails, start=1):
                status_icon = "📖" if email.read else "📨"
                self.log_to_display(f"{i}. {status_icon} {email}")
        
        self.update_status(f"Viewing inbox: {user_name}")
    
    def read_email_gui(self):
        """Read a specific email from current inbox"""
        if not self.current_user:
            messagebox.showerror("Error", "Please check an inbox first!")
            self.update_status("Error: No inbox selected")
            return
        
        if not self.current_inbox_emails:
            messagebox.showerror("Error", "No emails to read!")
            self.update_status("Error: Inbox empty")
            return
        
        index_str = simpledialog.askstring("Read Email", 
                                          f"Enter email number (1-{len(self.current_inbox_emails)}):")
        if not index_str:
            return
        
        try:
            index = int(index_str)
            if 1 <= index <= len(self.current_inbox_emails):
                email = self.current_inbox_emails[index - 1]
                self.clear_display()
                self.log_to_display(f"\n{'=' * 70}")
                self.log_to_display("📧 Email Details")
                self.log_to_display(f"{'=' * 70}")
                self.log_to_display(f"From:     {email.sender.name}")
                self.log_to_display(f"To:       {email.receiver.name}")
                self.log_to_display(f"Subject:  {email.subject}")
                self.log_to_display(f"Date:     {email.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
                self.log_to_display(f"{'=' * 70}\n")
                self.log_to_display(f"{email.body}\n")
                self.log_to_display(f"{'=' * 70}\n")
                
                email.mark_as_read()
                self.persistence.save_data(self.users)
                self.update_status(f"Reading email {index} from {self.current_user}")
            else:
                messagebox.showerror("Error", f"Please enter a number between 1 and {len(self.current_inbox_emails)}")
                self.update_status("Error: Invalid email number")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            self.update_status("Error: Invalid input")
    
    def delete_email_gui(self):
        """Delete a specific email from current inbox"""
        if not self.current_user:
            messagebox.showerror("Error", "Please check an inbox first!")
            self.update_status("Error: No inbox selected")
            return
        
        if not self.current_inbox_emails:
            messagebox.showerror("Error", "No emails to delete!")
            self.update_status("Error: Inbox empty")
            return
        
        index_str = simpledialog.askstring("Delete Email", 
                                          f"Enter email number to delete (1-{len(self.current_inbox_emails)}):")
        if not index_str:
            return
        
        try:
            index = int(index_str)
            if 1 <= index <= len(self.current_inbox_emails):
                # Confirm deletion
                email = self.current_inbox_emails[index - 1]
                confirm = messagebox.askyesno("Confirm Delete", 
                                            f"Delete email from {email.sender.name} about '{email.subject}'?")
                if confirm:
                    self.users[self.current_user].delete_email(index)
                    self.current_inbox_emails = self.users[self.current_user].inbox.emails
                    self.log_to_display(f"\n✅ Email {index} deleted successfully!\n")
                    self.persistence.save_data(self.users)
                    self.update_status(f"Email deleted from {self.current_user}")
            else:
                messagebox.showerror("Error", f"Please enter a number between 1 and {len(self.current_inbox_emails)}")
                self.update_status("Error: Invalid email number")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            self.update_status("Error: Invalid input")
    
if __name__ == '__main__':
    root = tk.Tk()
    gui = EmailSystemGUI(root)
    root.mainloop()
