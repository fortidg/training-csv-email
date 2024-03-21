import csv
import smtplib
import sys

# Add the path to the emailcreds.py file
sys.path.insert(1, '/home/ubuntu/Python/')
# Pull environment variables from emailcreds.py
from emailcreds import sender_acc, sender_pass

mailserver = smtplib.SMTP('smtp.gmail.com', 587)

def send_email(sender_acc, sender_pass, receiver_email, subject, message):
    try:
        server = mailserver
        server.connect('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_acc, sender_pass)
        server.sendmail(sender_acc, receiver_email, f"Subject: {subject}\n\n{message}")
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")
    finally:
        server.quit()

def generate_emails(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if present
        for row in reader:
            name = row[0]
            receiver_email = row[1]
            subject = row[2]
            username = row[3]
            password = row[4]
            message = f"Hi {name},\n\nYour FortiCloud credentials are as follows:\n\nusername - {username}\npassword - {password}\n\n Please login using the URL provided in the qwiklab instructions.\n\nBest regards,\nFortinet CSE"
            send_email(sender_acc, sender_pass, receiver_email, subject, message)

# Usage
csv_file = 'testcsv.csv'
generate_emails(csv_file)