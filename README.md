Use this script to send email using variables gleaned from a CSV file.

The "sys.path.insert" on line 5 is just pulling variables in from a python file in a different folder.  This was done just to keep email address and creds off of github.  You can omit this if you want to define those variables locally.
for example
sender_acc = "youremail@gmail.com"
sender_pass = "gmailpasskey"