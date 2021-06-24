import meet, display

#### This deals with the PayPal API calls

## Open Live Payments file

def read_lessons():
    print('reading payments')
    lessons = [{'id': '1', 'paid': 'n'},{'id':'2', 'paid': 'y'}, {'id':'3', 'paid': 'n'}]
    return  lessons

## Request Paypal Payment

def make_payment_request(lesson):
    pass

## Check Payment Status

def check_payment_status(lesson):
    print(f'checking payment status for lesson #{lesson["id"]}')
    print('Making Paypal API call...')
    if lesson['id'] == '3':
        print(f'Payment for lesson #{lesson["id"]} has been made.')
        return 'y'
    else:
        print(f'No payment for lesson #{lesson["id"]}')
        return 'n'
    

## Process Payments

def process_payments():
    lessons = read_lessons()
    for lesson in lessons:
        if lesson['paid'] == 'n':
            lesson['paid'] = check_payment_status(lesson)
            if lesson['paid'] == 'y':
                meet.create_Zoom(lesson)
    display.display_lessons(lessons) #display in 2 groups reverse chronologically: unpaid, paid
    print('\npayments processed!\n')         
    


