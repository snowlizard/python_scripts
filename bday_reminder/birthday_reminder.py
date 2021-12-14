import smtplib, datetime, json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# uses the BIRTHDAYS dictionary and date time to check if
# today is a persons' birthday and if it is the program uses
# your email to send yourself an sms (text message) reminding
# you to tell that person Happy Birthday!

# SMPT providers
# AT&T   : smtp.mail.att.net
# Comcast: smtp.comcast.net
# iCloud : smtp.mail.me.com
# Gmail  : smtp.gmail.com
# Outlook: smtp-mail.outlook.com
# Yahoo  : smtp.mail.yahoo.com

# phone carrier sms gateways
# AT&T        : [number]@txt.att.net
# Sprint      : [number]@messaging.sprintpcs.com
# Sprint      : [number]@pm.sprint.com
# Tmobile     : [number]@tmomail.net
# Verizon     : [number]@vtext.com
# Boost Mobile: [number]@myboostmobile.com
# Cricket     : [number]@sms.mycricket.com
# Metro PCS   : [number]@mymetropcs.com

try:
    file = open("birthdays.json")
    BRITHDAYS = json.load(file)
    file.close()
except Exception as Error:
    print(Error.args[1])
    exit()

# Credentials
my_email = "redacted@gmail.com"
email_password = 'redacted'
mail_server = 'smtp.gmail.com'
# using tmobile as phone carrier
my_number = '+1redacted@tmomail.net'

# Connection
try:
    connection = smtplib.SMTP(mail_server, 587)
    connection.starttls()
    connection.login(my_email, email_password)
except Exception as Error:
    print(Error.args[1])
    connection.close()
    exit()

# todays date by month and day only
this_month = datetime.datetime.now().today().month
this_day = datetime.datetime.now().today().day
today = str(this_month)  + " " + str(this_day)

# check if today matches a persons birthday
for key, value in BRITHDAYS.items():
    print(key, value)
    if value == today:
        # Content
        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = my_number
        msg['Subject'] = "Birthday"
        body = f"Remember to tell {key} happy birthday.\n"
        msg.attach(MIMEText(body, 'plain'))
        sms = msg.as_string()

        # send message
        connection.sendmail(my_email, my_number, sms)

connection.close()