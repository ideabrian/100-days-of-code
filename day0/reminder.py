## Send a reminder via SMS
 # for #100DaysOfCode

user = '<username>' # your gmail username e.g. <username>@gmail.com
pwd = '' # your gmail password ( be sure not to commit this to github )
         # I have security turned on, so I created a specific App Password for this purpose.
recipient = '<your_phone_number>@text.att.net' # this sends an email to text if you're an ATT customer
subject = '100DaysOfCode'
body = '''Are you ready for 100 days of code? <your reminder message here>'''


# Google search to find code on Stack Overflow
# http://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        # server = smtplib.SMTP("smtp.gmail.com", 587)
        # server.ehlo()
        # server.starttls()
        # server.login(gmail_user, gmail_pwd)
        # server.sendmail(FROM, TO, message)
        # server.close()
        # print 'successfully sent the mail'
        # SMTP_SSL Example
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo() # optional, called by login()
        server_ssl.login(gmail_user, gmail_pwd)
        # ssl server doesn't support or need tls, so don't call server_ssl.starttls()
        server_ssl.sendmail(FROM, TO, message)
        #server_ssl.quit()
        server_ssl.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

# call the function
send_email(user, pwd, recipient, subject, body)