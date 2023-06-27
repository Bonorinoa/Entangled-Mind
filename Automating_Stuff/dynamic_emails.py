import smtplib
import ssl
import pandas as pd
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

### SETUP ### 
# Do not use email as a name for neither the file or any functions or variables to avoid conflicts with the email module

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

### WORK ###
## Dynamic Email ##
import random
from faker import Faker
import pandas as pd

fake = Faker()

# Generate random data
data = []
for _ in range(10):
    name_employee = fake.name()
    email_employee = fake.email()
    project_title = fake.catch_phrase()
    project_deadline = fake.date_between_dates(date_start=datetime(2023,4,1), date_end=datetime(2023,8,25))
    
    data.append([name_employee, email_employee, project_title, project_deadline])

# Create a pandas dataframe
columns = ['nameEmployee', 'emailEmployee', 'projectTitle', 'projectDeadline']
dataset = pd.DataFrame(data, columns=columns)

### EMAIL ###
email_from = "agbonorino21@gmail.com" # Email to send from
email_to = "agbonorino21@gmail.com" # Email to send to

pswd = "vftmpdokgxgqssit"       # App password for gmail

simple_email_context = ssl.create_default_context()

def create_message(project):
    '''Creates the message to be sent and extracts email to send to'''
    emp_email = project['emailEmployee']
    
    days_left = (project['projectDeadline'] - datetime.now().date()).days
    
    message = f""" 
    Hello {project["nameEmployee"]},
    This is a reminder that your project "{project["projectTitle"]}" is {f"to be presented in {days_left} days" if days_left > 0 else f"late, please submit the document or reply to this email to apply for an extension."}. \n
    Best regards, \n
    John Doe
    """
    return message, emp_email

### SEND EMAIL ###
logs = []

try:
    # Connect to the server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from, pswd)
    print("Connected to server :-)")
    
    # Create the MIMEText object with the message and encoding
    for idx in range(len(dataset)):

        # create the message to be sent and extract the email to send to
        # Since these emails are fake, I will create a log of emails to be sent and email the txt file to myself
        message, emp_email = create_message(dataset.iloc[idx,:])

        # Create the MIMEText object with the message and encoding
        msg = MIMEMultipart()
        msg.attach(MIMEText(message, "plain", "utf-8"))
        msg["From"] = email_from
        msg["To"] = email_to
        msg["Subject"] = "Reminder: Project Deadline"

        # Send email and print confirmation in the terminal
        print()
        print(f"Sending email to - {email_to}")
        TIE_server.send_message(msg)
        print(f"Email succesfully sent to - {email_to}")

        # save the logs to keep a simple database of the emails sent
        logs.append(f"The following email has been sent to {email_to} at {datetime.now()}: \n\n {message} \n\n ----------------")

    with open(r'emails_logs.txt', 'w') as fp:
        for log in logs:
            # write each item on a new line
            fp.write("%s\n" % log)
        print('Done. Emailing logs...')
    
    # Send the logs to myself
    attachment = open(r'emails_logs.txt', 'rb')
    # encode as base64
    attachment_package = MIMEBase('application', 'octet-stream')
    attachment_package.set_payload((attachment).read())
    encoders.encode_base64(attachment_package)
    attachment_package.add_header('Content-Disposition', "attachment; filename= emails_logs.txt")
        
    msg_logs = MIMEMultipart()
    msg_logs["From"] = email_from
    msg_logs["To"] = email_to
    msg_logs["Subject"] = "Email Logs"
    
    # attach the txt file to the email
    msg_logs.attach(attachment_package)
    # cast as string
    text = msg_logs.as_string()
    # send the email
    TIE_server.sendmail(email_from, email_to, text)
    print('Logs emailed succesfully')
    
# If there's an error, print it out
except Exception as e:
    print(e)

# Close the port
finally:
    TIE_server.quit()
    