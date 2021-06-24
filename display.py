# These functions deal with displaying information in CLI

## Check Payment Display

def display_lessons(lessons):
    print('displaying lesson payment info')
    unpaid_lessons = []
    paid_lessons = []
    for lesson in lessons:
        if lesson['paid'] == 'n':
            unpaid_lessons.append(lesson)
        elif lesson['paid'] == 'y':
            paid_lessons.append(lesson)
    for lesson in unpaid_lessons:
        print(f'Lesson #{lesson["id"]} remains unpaid.')
    for lesson in paid_lessons:
        print(f'Lesson #{lesson["id"]} has been paid for.')
    print('OK!')
    