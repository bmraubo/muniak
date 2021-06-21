#### Store transaction data in persistent JSON

def unpack_json():
    pass

def pack_json():
    pass

#### Load settings file

def load_settings():
    # parses settings.json and loads values into settings variables
    # settings:
    # host_name, host_email
    # manual_checks - human confirmation of zoom call
    pass

def save_settings():
    pass

#### Main menu

def main_menu():
    global exit_code
    # Set up New Lesson
        # lesson_info = create_lesson()
        # Lesson(lesson_info)
    # Check Payment Status
        # live_transactions = all transactions that are pending or completed (up to day after lesson)
        # pending_transactions = list of payments requested but not made
        # for transaction in pending_transactions: check_payment_status
        # Checks for completed transactions
        # If a transaction is complete, creates a meeting
        # Displays list of created meetings
        # Outstanding payments listed in order of proximity to lesson
    # Add new student
    # Create Report
        # Generates Report and emails it to selected admin
        # Export all user data by email to host/admin account
    # Settings
    # Exit the app
        
    pass

if __name__ == "__main__":
    exit_code = 0
    load_settings()
    while exit_code == 0:
        main_menu()

