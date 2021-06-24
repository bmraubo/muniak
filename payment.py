import meet, display

#### This deals with the PayPal API calls

## Open Live Payments file

def read_lessons():
    print('reading lessons.json')
    lessons = [{'id': '1', 'paid': 'n'}, {'id':'2', 'paid': 'y'}, {'id':'3', 'paid': 'n'}]
    return  lessons

## Request Paypal Payment

def make_payment_request(lesson):
    pass

## Check Payment Status - Paypal

def check_payment_status(lesson):
    print(f'checking payment status for lesson #{lesson["id"]}')
    print('Making Paypal API call...')
    if lesson['id'] == '3': ## if payment made, make a note
        print(f'Payment for lesson #{lesson["id"]} has been made.')
        meet.create_Zoom(lesson)
        return 'y'
    else:
        print(f'No payment for lesson #{lesson["id"]}')
        return 'n'

## Generate Payment Request Email

def request_wise_payment(lesson):
    #generate payment ref - can just be increasing integers
    #perhaps payment id should be linked to student, not to lesson
    #this would avoid confusion for the student, since they would not have to change id each time 
    #problem is what if they pay for more than one lesson at once?
    #concept of credit could play a role 
    #saves ref to lesson["student"]["id"]
    #generates email requesting payment and sends
    pass

## Check Payment Status - Wise

def get_wise_payments():
    print('When was the last check?')
    print('Get transactions since last check')
    print('note time and date in settings.json')
    #returns payments

def check_wise_payments(lesson, payments):
    # if the reference of a transaction matches a lesson, checks payment amount
    print('check lesson id against payment refs')
    if lesson['id'] == '3': ## if payment made, make a note
        print(f'Payment for lesson #{lesson["id"]} has been made.')
        meet.create_Zoom(lesson)
        return 'y' # if payment amount is correct, returns 'y' to lesson['paid']
    else:
        print(f'No payment for lesson #{lesson["id"]}')
        return 'n'
    

## Process Payments

def process_payments():
    payments = get_wise_payments()
    lessons = read_lessons()
    for lesson in lessons:
        if lesson['paid'] == 'n':
            lesson['paid'] = check_wise_payments(lesson, payments)
                
    display.display_lessons(lessons) #display in 2 groups reverse chronologically: unpaid, paid
    print('\npayments processed!\n')         
    


