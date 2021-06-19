#### Store transaction data in persistent JSON

def unpack_json():
    pass

def pack_json():
    pass

#### Load settings file

def load_settings():
    # parses settings.json and loads values into settings variables
    pass

def save_settings():
    pass

#### Main menu

def main_menu():
    global exit_code
    # Set up New Lesson
    # Check Payment Status
        # Checks from completed transactions
        # If a transaction is complete, creates a meeting
        # Displays list of created meetings
        # Outstanding payments listed in order of proximity to lesson
    # Create Report
        # Generates Report and emails it to selected admin
    # Settings
    # Exit
        #exit_code = 1
        
    pass

if __name__ == "__main__":
    exit_code = 0
    load_settings()
    while exit_code == 0:
        main_menu()

