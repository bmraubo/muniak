# muniak
An automated assistant for music teachers

---
### What it is

A CLI application to help musicians teaching through Zoom automate arranging payment for lessons and organizing Zoom meetings.

It will:
- Allow input of lesson for student
- Generate Payment Request
- Validate Payment
- On successful validation, email Zoom link to user.

Additionally it will:

- Print out a list of pending transactions
- Generate a reminder email if payment hasn't been made a set period before the lesson
- Generate a summary email for all activities done that day and send it to host

### How it will work

The app with keep track of all students - when a lesson is arranged, the app creates a payment request and sends it to the student. 

When the student pays, the app creates a Zoom meeting and emails the link to the student and the host.

Once this is accomplished and working, expansion is possible.

How the app should be run - it would be good to have some persistent state that checks for PayPal payments (and auto generates Zoom meetings) with user intervention to create new lessons.

As a first step, I will set it up to be wholly initialised by the user. Let things grow from there if the fundamentals work.

**Remember that security will be important here - Authorisation will have to be handled securely**

#### Main menu

Will use PyInquirer

#### Store info in persistent JSON

#### Input interface to arrange lesson

Input interface to add object to Lesson class. 

#### PayPal API Call - Request

#### PayPal API Call - Confirm

#### Zoom API Call - Arrange Meeting

#### Generate Email
