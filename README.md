# 📧 Email System

A fully-featured email system built with Python and Tkinter with data persistence, a beautiful GUI, and complete email management capabilities.

## 🎯 Features

- ✅ **User Management** - Create multiple user accounts
- ✅ **Send Emails** - Send messages between users with subject and body
- ✅ **Rich GUI** - Beautiful Tkinter interface with modern styling
- ✅ **Read/Unread Tracking** - Track which emails have been read
- ✅ **Email Details** - View full email content with timestamps
- ✅ **Delete Emails** - Remove emails from inbox with confirmation
- ✅ **Data Persistence** - Save and load all emails from JSON file
- ✅ **Status Bar** - Real-time feedback on actions
- ✅ **Scrollable Display** - Large text area with scrollbar for viewing emails

## 📋 Requirements

- Python 3.6+
- Tkinter (included with Python)
- No external dependencies!

## 🚀 Quick Start

```bash
python3 email_system.py
```

The Email System GUI window will open with a welcome message and available commands.

## 📖 How to Use

### 1. **Create User**
- Click "Create User" button
- Enter a username
- User account is created immediately

### 2. **Send Email**
- Click "Send Email" button
- Enter sender name (must be an existing user)
- Enter receiver name (must be an existing user)
- Enter email subject
- Enter email message body
- Email is sent and saved to receiver's inbox

### 3. **Check Inbox**
- Click "Check Inbox" button
- Enter username
- View all emails in that user's inbox
- Shows read/unread status and timestamps

### 4. **Read Email**
- First check a user's inbox
- Click "Read Email" button
- Enter the email number to read
- View full email details including:
  - From, To, Subject, Date
  - Complete message body
- Email is automatically marked as read

### 5. **Delete Email**
- First check a user's inbox
- Click "Delete Email" button
- Enter the email number to delete
- Confirm deletion
- Email is removed from inbox

### 6. **Clear Display**
- Click "Clear Display" to empty the text area
- Useful for cleaning up the screen

## 🏗️ Architecture

### Classes

**Email**
- Stores email information: sender, receiver, subject, body, timestamp
- Tracks read/unread status
- Provides string representation with status indicator

**Inbox**
- Manages collection of emails
- Methods to receive, list, read, and delete emails
- Index validation for safe operations

**User**
- Represents a user account
- Has an associated inbox
- Methods to send, check, read, and delete emails

**EmailSystemGUI**
- Tkinter-based graphical interface
- Handles all user interactions
- Integrates data persistence
- Provides styled buttons and display area

**DataPersistence**
- Handles saving/loading data to JSON
- Persists across application restarts
- Located in `data_persistence.py`

## 💾 Data Storage

All email data is automatically saved to `email_data.json` in the same directory. The format looks like:

```json
{
  "Alice": {
    "emails": [
      {
        "from": "Bob",
        "to": "Alice",
        "subject": "Hello",
        "body": "Hi Alice!",
        "timestamp": "2026-04-19T10:30:45.123456",
        "read": true
      }
    ]
  }
}
```

## 🎨 GUI Design

- **Modern Color Scheme**: Green buttons, dark title bar, clean white text area
- **Responsive Layout**: Buttons organized in grid, expandable text display
- **Status Bar**: Real-time feedback on all actions
- **Scrollable Area**: Large text area with scrollbar for viewing emails
- **Emoji Icons**: Visual indicators for emails (📨 unread, 📖 read)

## 📚 Project Structure

```
email_system/
├── email_system.py          # Main application with GUI
├── data_persistence.py      # Data storage and retrieval
├── README.md               # This file
├── requirements.txt        # Dependencies (Python standard library)
└── .gitignore             # Git ignore file
```

## 🔧 Technical Details

### Technology Stack
- **Language**: Python 3
- **GUI Framework**: Tkinter
- **Data Storage**: JSON
- **File System**: Built-in modules (json, os, datetime)

### Code Patterns
- Object-Oriented Programming (OOP)
- Model-View separation (core logic vs GUI)
- Data persistence layer abstraction
- Exception handling for invalid inputs

## 🚀 Future Improvements

- Email folders (Inbox, Sent, Drafts, Trash)
- Search functionality
- Email attachments
- Email threading/replies
- User authentication
- Database backend (SQLite)
- Web interface (Flask)

## 📝 License

MIT License - Free to use and modify

## 👨‍💻 Author Notes

This project demonstrates:
- Python OOP principles
- Tkinter GUI development
- Data persistence patterns
- Clean code organization
- Professional README documentation

Perfect for portfolio and learning purposes!
