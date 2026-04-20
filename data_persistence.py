import json
import os
from datetime import datetime

class DataPersistence:
    """Handles saving and loading email data to/from JSON files"""
    
    def __init__(self, data_file='email_data.json'):
        self.data_file = data_file
        self.data = self.load_data()
    
    def load_data(self):
        """Load existing email data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_data(self, users_dict):
        """Save email data to JSON file"""
        data_to_save = {}
        for username, user in users_dict.items():
            emails = []
            for email in user.inbox.emails:
                emails.append({
                    'from': email.sender.name,
                    'to': email.receiver.name,
                    'subject': email.subject,
                    'body': email.body,
                    'timestamp': email.timestamp.isoformat(),
                    'read': email.read
                })
            data_to_save[username] = {'emails': emails}
        
        with open(self.data_file, 'w') as f:
            json.dump(data_to_save, f, indent=2)
    
    def get_user_data(self, username):
        """Get saved emails for a specific user"""
        return self.data.get(username, {}).get('emails', [])
    
    def clear_data(self):
        """Clear all saved data"""
        if os.path.exists(self.data_file):
            os.remove(self.data_file)
        self.data = {}
