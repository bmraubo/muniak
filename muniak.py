import PyInquirer as inq
import report, payment

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

# Reports Menu

def reports_menu():
    options = [{
        'type': 'list',
        'name': 'View Reports',
        'message': 'Pick an option',
        'choices': [
            'Daily Report',
            'Export all Data',
            'Back'
            ]
    }]
    choice = inq.prompt(options)
    print(choice['View Reports'])
    report_menu_choice(choice)

def report_menu_choice(choice):
    if choice['View Reports'] == 'Daily Report':
        print('PLACEHOLDER: generate daily report...')
        report.generate_daily_report('hello@world.com')
    elif choice['View Reports'] == 'Export all Data':
        report.export_data('hello@world.com')
    else:
        pass

# Main Menu

#### Main Menu choices

def main_menu_choice(choice):
    global exit_code
    if choice['Main Menu'] == 'Set up New Lesson':
        print('PLACEHOLDER:\tSet up New Lesson')
    elif choice['Main Menu'] == 'Process Payments':
        payment.process_payments()
    elif choice['Main Menu'] == 'View Lesson':
        print('PLACEHOLDER:\tView Lesson')
    elif choice['Main Menu'] == 'Add New Student':
        print('PLACEHOLDER:\tAdd New Student')
    elif choice['Main Menu'] == 'Reports':
        reports_menu()
    else:
        print('EXITING APP')
        exit_code = 1

#### Main menu

def main_menu():
    options = [{
        'type': 'list',
        'name': 'Main Menu',
        'message': 'Pick an option',
        'choices': [
            'Set up New Lesson',
            'Process Payments',
            'View Lesson',
            'Add New Student',
            'Reports',
            'Exit'
            ]
    }]
    choice = inq.prompt(options)
    print(choice['Main Menu'])
    main_menu_choice(choice)
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

